import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import sys

from mcap_protobuf.decoder import DecoderFactory
from mcap.reader import make_reader, McapReader
from mcap.reader import make_reader


vn_lat_lon_data_list = []


latitudes = []
longitudes = []


with open(sys.argv[1], "rb") as f:
    reader = make_reader(f, decoder_factories=[DecoderFactory()])
    for schema, channel, message, proto_msg in reader.iter_decoded_messages(topics=["vn_lat_lon_data"]):
        # message
        # if (message.log_time > 0) and (message.log_time <):
        # print(message.log_time)
        log_time = message.log_time / 1e9
        # print(log_time)
        if (log_time > 1690575125.989472210) and (log_time < 1690575199.989472210):
            latitudes.append(proto_msg.vn_gps_lat)
            longitudes.append(proto_msg.vn_gps_lon)
        # message
        # print(f"{proto_msg}")


# # Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# # Create a Basemap instance
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c', ax=ax)

# Draw coastlines and countries
m.drawcoastlines()
m.drawcountries()

# Convert latitude and longitude to x and y coordinates
x, y = m(longitudes, latitudes)

# Plot the points
m.scatter(x, y, s=10,marker='o', color='red', zorder=1)

# Add title
plt.title('Latitude and Longitude Points')

# Show the plot
plt.show()
