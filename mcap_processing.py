# TODO get start and end times based on specific value of a topic (eg: CAR_STATE)

import sys
from pathlib import Path
import io
import os
import glob

from mcap_protobuf.decoder import DecoderFactory
from mcap.reader import make_reader, McapReader


def get_min_value(time_series_msgs, attr_name):
    return min(getattr(msg, attr_name) for msg in time_series_msgs)


# when braking, our front sus. pots should shorten
# def analyze_sus_pots(sus_pot_timseries_msgs, ):

def get_all_msgs_from_mcap_threaded(mcap_reader, num_threads):
    stats = mcap_reader.get_summary().statistics
    duration = (stats.message_end_time - stats.message_start_time)
    
    
def get_topic_msgs_from_mcaps(mcap_readers, topic):
    msgs = []
    for reader in mcap_readers:
        for schema_, channel_, message_, proto_msg in reader.iter_decoded_messages(topics = [topic]):
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
            file = open(os.path.join(os.getcwd(), file_path), 'rb')
            reader = make_reader(file, decoder_factories=[DecoderFactory()])
            mcap_readers.append(reader)
        except:
            print("error: couldnt open file path: ", file_path)
            pass
    return mcap_readers

def main():
    mcap_readers = open_files_in_folder(sys.argv[1])
    topics = ["mcu_suspension_data", "sab_suspension_data"]
    
    # for topic in topics:
    # topic = "sab_suspension_data"
    # msgs = get_topic_msgs_from_mcaps(mcap_readers, topic)
    # print("min potentiometer_rl value for: ", topic, " is: ", get_min_value(msgs, "potentiometer_rl"))
    # msgs = get_topic_msgs_from_mcaps(mcap_readers, topic)
    # print("min potentiometer_rr value for: ", topic, " is: ", get_min_value(msgs, "potentiometer_rr"))
    
    for reader in mcap_readers:
        get_all_msgs_from_mcap_threaded(reader, 3)
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