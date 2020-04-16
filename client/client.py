import json
import socket
import struct

form_data = json.dumps({
    'client_name': "virtual_server",
    'status': "succcess"
})
head_bytes = bytes(form_data, encoding='utf-8')
head_len_bytes = struct.pack('i', len(form_data))

s = socket.socket()  # 创建 socket 对象
host = '10.0.0.5'  # 获取本地主机名
port = 8080  # 设置端口号

s.connect((host, port))
s.send(head_len_bytes)
s.send(head_bytes)

s.close()
