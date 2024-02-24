Bandwidth = 33000;
schannel_bandwidth = 25;
channel_bandwidth = 2*schannel_bandwidth;
print(f'Channel Bandwidth - {channel_bandwidth}')
TotalChannel = (Bandwidth/channel_bandwidth);
print(f'Total Channel - {TotalChannel}')
ControlChannelBandwidth = 1000;
Total_control_channel = (ControlChannelBandwidth/channel_bandwidth)
print(f'Total Control Channel - {Total_control_channel}')
ReuseCellList = [4, 7, 12]
for i in ReuseCellList:
    channel = TotalChannel/i
    control_channel = round(Total_control_channel/i)
    voice_channel = round((TotalChannel-Total_control_channel)/i)
    print(f'Reuse {i} and Channel Per Cell '
          f'{round(channel)}')
    print(f'Control Channel {control_channel} and voice channel {voice_channel}')

