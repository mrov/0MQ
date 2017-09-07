# coding=utf-8
import zmq
import time
# Envia o Nome do server e o endereço para o lookup
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
json_msg = {"type": "POST", "route": "Adress/",
            "name": "B", "Adress": "tcp://localhost:5557"}
socket.send_json(json_msg)
msg = socket.recv_json()
print msg['code']
