import sys
from mcap.reader import make_reader
from mcap_protobuf.decoder import DecoderFactory


with open(sys.argv[1], "rb") as f:

    reader = make_reader(f, decoder_factories=[DecoderFactory()])
    for schema_, channel_, message_, proto_msg in reader.iter_decoded_messages():
        print(proto_msg)