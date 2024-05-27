# TODO get start and end times based on specific value of a topic (eg: CAR_STATE)

import sys
from pathlib import Path
import io
import os
import glob
from typing import Any
from mcap_protobuf.decoder import DecoderFactory
from mcap.reader import make_reader, McapReader
import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt

class MCAPMessage:
    def __init__(self, schema, channel, message, proto_msg):
        self.schema = schema
        self.channel = channel
        self.message = message
        self.proto_msg = proto_msg
        self.log_time = message.log_time

def merge_dictionaries(*dicts):
    merged_dict = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in merged_dict:
                merged_dict[key].extend(value)
            else:
                merged_dict[key] = value.copy()
    return merged_dict

def convert_dict_to_pandas_df(all_msgs_dict: dict) -> pd.DataFrame:
    records = []
    for topic, messages in all_msgs_dict.items():
        for msg in messages:
            record = {
                'topic': topic,
                'schema': msg.schema,
                'channel': msg.channel,
                'message': msg.message,
                'proto_msg': msg.proto_msg,
                'log_time': pd.Timestamp(msg.log_time, unit='ns')
            }
            records.append(record)

    # Create the DataFrame
    df = pd.DataFrame(records)

    return df

def get_start_end_times(msg_df: pd.DataFrame, filter_topic: str, topic_attr_name: str, target_value: Any) -> list[tuple]:
    """_summary_

    Args:
        msgs (dict): _description_
        filter_topic (str): _description_
        topic_attr_name (str): _description_

    Returns:
        list[tuple]: _description_
    """
    msgs = msg_df[msg_df['topic'] == filter_topic]

    # Extract the member variable into a new column for easy comparison
    msgs[topic_attr_name] = msgs['proto_msg'].apply(lambda x: getattr(x, topic_attr_name))
    shifted_member_var = msgs[topic_attr_name].shift(1)
    mask = msgs[topic_attr_name] != shifted_member_var
    transitions = msgs[mask][['log_time', topic_attr_name]].to_numpy()

    start_times = []
    end_times = []
    in_period = False
    for transition in transitions:
        if (transition[1] == target_value) and (not in_period):
            in_period = True
            start_times.append(transition[0])
        elif (transition[1] is not target_value) and in_period:
            in_period = False
            end_times.append(transition[0])

    if(len(start_times) > len(end_times)):
        end_times.append(max(msgs[msg_df['log_time']]))

    return list(zip(start_times, end_times))

def get_min_value(time_series_msgs, attr_name):
    """get the min value in a list or array of time series msgs

    Args:
        time_series_msgs (_type_): list / array type of time series msgs
        attr_name (_type_): float / int attribute of the message that will be used to get the minimum value from

    Returns:
        _type_: min value of same attribute type 
    """
    return min(getattr(msg, attr_name) for msg in time_series_msgs)

def get_all_msgs_from_mcap(mcap_reader) -> list[MCAPMessage]:
    msgs = {}
    for schema_, channel_, message_, proto_msg in mcap_reader.iter_decoded_messages():
        if channel_.topic not in msgs:
            msgs[channel_.topic] = []
        msgs[channel_.topic].append(MCAPMessage(schema_, channel_, message_, proto_msg))
    return msgs

def get_topic_msgs_from_mcaps(mcap_readers, topic):
    msgs = []
    for reader in mcap_readers:
        for schema_, channel_, message_, proto_msg in reader.iter_decoded_messages(
            topics=[topic]
        ):
            msgs.append(proto_msg)
    return msgs

def open_files_in_folder(folder_path: str) -> list[McapReader]:
    # Create the full search pattern
    search_pattern = os.path.join(folder_path, "*.mcap")

    # Get a list of all files matching the pattern
    files = glob.glob(search_pattern)
    # print(files)
    # Check if files are found
    if not files:
        print(f"No files matching *.mcap found in {folder_path}")
        return

    # Iterate through the files and open each one
    mcap_readers = []
    for file_path in files:
        try:
            print(os.path.join(os.getcwd(), file_path))
            file = open(os.path.join(os.getcwd(), file_path), "rb")
            reader = make_reader(file, decoder_factories=[DecoderFactory()])
            mcap_readers.append(reader)
        except:
            print("error: couldnt open file path: ", file_path)
            pass
    return mcap_readers, files

def time_plot_msg_member(df, topic, pb_msg_member):
    msgs = df[df['topic'] == topic]
    msgs[pb_msg_member] = msgs['proto_msg'].apply(lambda x: getattr(x, pb_msg_member))
    msgs.plot(x='log_time', y=pb_msg_member)
    print(msgs)
    plt.show()
    
# when braking, our front sus. pots should shorten
def analyze_sus_pots(msgs_df):
    rear_sus_pot_data = msgs_df[msgs_df['topic'] == 'sab_suspension_data']
    front_sus_pot_data = msgs_df[msgs_df['topic'] == 'mcu_suspension_data']
    pedals_data = msgs_df[msgs_df['topic']=='mcu_pedal_readings_data']
    # print(pedals_data)
    time_plot_msg_member(msgs_df, 'mcu_suspension_data', 'potentiometer_fr')

def get_important_data_for_times(df, important_times):
    conditions = [(df["log_time"] >= start) & (df["log_time"] <= end) for start, end in important_times]
    combined_condition = reduce(lambda x, y: x | y, conditions)
    return df[combined_condition]

def main():
    mcap_readers, files = open_files_in_folder("/home/ben/mcap_analysis/mcaps/raw")
    # topics = ["mcu_suspension_data", "sab_suspension_data"]
    # for topic in topics:
    # topic = "sab_suspension_data"
    # msgs = get_topic_msgs_from_mcaps(mcap_readers, topic)
    # print("min potentiometer_rl value for: ", topic, " is: ", get_min_value(msgs, "potentiometer_rl"))
    # msgs = get_topic_msgs_from_mcaps(mcap_readers, topic)
    # print("min potentiometer_rr value for: ", topic, " is: ", get_min_value(msgs, "potentiometer_rr"))
    msgs_total = {}
    for reader in mcap_readers:
        msgs_total = merge_dictionaries(msgs_total, get_all_msgs_from_mcap(reader))
    df = convert_dict_to_pandas_df(msgs_total)
    important_times = get_start_end_times(df, "mcu_status_data", "ecu_state", "5")
    cut_df = get_important_data_for_times(df, important_times)
    analyze_sus_pots(cut_df)
    # topic = "mcu_suspension_data"
    # msgs = get_topic_msgs_from_mcaps(mcap_readers, topic)
    # print("min potentiometer_fl value for: ", topic, " is: ", get_min_value(msgs, "potentiometer_fl"))
    # msgs = get_topic_msgs_from_mcaps(mcap_readers, topic)
    # print("min potentiometer_fr value for: ", topic, " is: ", get_min_value(msgs, "potentiometer_fr"))

    # print(mcap_readers)
    # for schema_, channel_, message_, proto_msg in mcap_readers[0].iter_decoded_messages():
    #     print(proto_msg)
    #
    # for topic_name in topics:
    #     get_topic_msgs_from_mcaps(mcaps, topic_name)


if __name__ == "__main__":
    main()
