

from mcap_processing import open_files_in_folder, merge_dictionaries
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import concurrent.futures
import multiprocessing
from queue import Empty
import copy

class MCAPMessage:
    def __init__(self, schema, channel, message, proto_msg):
        self.schema = schema
        self.channel = channel
        # self.message = message
        self.log_time = message.log_time
        
        # Iterate over attributes of proto_msg and set them as attributes of MCAPMessage
        for attr_name in dir(proto_msg):
            if not attr_name.startswith("__") and not callable(getattr(proto_msg, attr_name)):
                setattr(self, attr_name, getattr(proto_msg, attr_name))
        print(dir(self))

def get_all_msgs_from_mcap(mcap_reader) -> list[MCAPMessage]:
    msgs = {}
    for schema_, channel_, message_, proto_msg in mcap_reader.iter_decoded_messages():
        if channel_.topic not in msgs:
            msgs[channel_.topic] = []
        msgs[channel_.topic].append(MCAPMessage(schema_, channel_, message_, proto_msg))
    return msgs

def convert_dict_to_pandas_df_zero_aligned_seconds(all_msgs_dict: dict, last_end_time=None) -> pd.DataFrame:
    records = []
    evaluating_first_recorded_msg = True
    first_time = 0
    prev_log_time_ns = 0
    curr_diff = 0
    log_time = 0
    # logic flow:
    #     if we are the first mcap being accumulated in the list of mcaps, we set our start time to 0 and look at the difference in msg.log_time between 
    #     the previous msg.log_time and the current msg.log_time. This difference is accumulated and the current accumulated time is the new log_time.
    #      if we are not the first mcap being accumulated, our first time is the last_end_time (ns). 
    for topic, messages in all_msgs_dict.items():
        for msg in messages:
            if not evaluating_first_recorded_msg:
                curr_diff = (msg.log_time - prev_log_time_ns) + curr_diff
            
            if last_end_time is not None:
                log_time = curr_diff + last_end_time
            else:
                log_time = curr_diff
            record = {
                'topic': topic,
                'schema': msg.schema,
                'channel': msg.channel,
                'message': msg.message,
                'proto_msg': msg.proto_msg,
                'log_time': (float(log_time) / 1.0e9)
            }
            prev_log_time_ns = msg.log_time
            records.append(record)

    # Create the DataFrame
    df = pd.DataFrame(records)
    return df, log_time

def process_reader(reader, queue, errors):
    try:
        ret_dict = get_all_msgs_from_mcap(reader)
        queue.put(copy.deepcopy(ret_dict))
    except Exception as e:
        errors.append((reader, e))

mcap_readers, files = open_files_in_folder("./mcaps/testing_multi_mcap")
queue = multiprocessing.Queue()
errors = multiprocessing.Manager().list()

processes = []
for reader in mcap_readers:
    process = multiprocessing.Process(target=process_reader, args=(reader, queue, errors))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

msgs_total = {}
while True:
    try:
        ret_dict = queue.get_nowait()
        print(len(ret_dict))
        msgs_total = merge_dictionaries(msgs_total, ret_dict)
    except Empty:
        break

all_msgs_df = convert_dict_to_pandas_df_zero_aligned_seconds(msgs_total)