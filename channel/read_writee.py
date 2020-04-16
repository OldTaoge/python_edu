fo = open("channel", "r", encoding='UTF-8')
str = fo.read()
ChannelCount = int(str.split("ChannelCount','", 1)[1].split("');")[0])
Channels = []
sp = str.split('ChannelName="', 1)[1].split('"', 1)
Channels.append({sp[0]: sp[1].split('ChannelSDP="', 1)[1].split('"')[0]})
for i in range(1, ChannelCount):
    sp = sp[1].split('ChannelName="', 1)[1].split('"', 1)
    Channels.append({sp[0]: sp[1].split('ChannelSDP="', 1)[1].split('"')[0]})
fo.close()

fo = open("channel.txt", "w", encoding='UTF-8')
for Channel in Channels:
    for key, value in Channel.items():
        fo.write(key + "," + "http://10.0.0.1:4022/udp/" + value[7:] + '\n')
