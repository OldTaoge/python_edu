import json
import socket
import struct
import signal
import os


def exit_f(signum, frame):
    print("exit")
    os._exit(0)


def get_data(connect):
    head_len_bytes = connect.recv(4)  # 先收报头4个bytes,得到报头长度的字节格式
    head_len = struct.unpack('i', head_len_bytes)[0]  # 提取报头的长度

    head_bytes = connect.recv(head_len)  # 按照报头长度x,收取报头的bytes格式
    header = json.loads(head_bytes)  # 提取报头
    return header


signal.signal(signal.SIGTERM, exit_f)
s = socket.socket()
host = '10.0.0.5'
port = 8080
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    o = get_data(c)
    if o["client_name"] == "virtual_server":
        print("虚拟机开机成功")

    c.close()
