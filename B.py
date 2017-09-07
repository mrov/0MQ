# coding=utf-8
import zmq
import time
# Envia o Nome do server e o endereço para o lookup
context = zmq.Context()
lookup_socket = context.socket(zmq.REQ)
lookup_socket.connect("tcp://localhost:5555")
print("B ready!!")
json_msg = {"type": "POST", "route": "Adress/",
            "name": "B", "Adress": "tcp://localhost:5558"}
lookup_socket.send_json(json_msg)
msg = lookup_socket.recv_json()
print msg['code']

tasks_B = []

# abre um socket para receber as tarefas do C1 e salva na lista tasks_B
C1_socket = context.socket(zmq.REP)
C1_socket.bind("tcp://*:5558")
req = C1_socket.recv_json()
tasks_B = req['Tasks']
res = {"code": "400"}
C1_socket.send_json(res)
print(tasks_B)


B_push_socket = context.socket(zmq.PUSH)
B_push_socket.bind("tcp://127.0.0.1:5560")
# Botão para confirmar que os trabalhadores estão online
raw_input("Type any key then press Enter when B workers are ready!\n")
for task in tasks_B:
    json_msg = {"task": task}
    B_push_socket.send_json(json_msg)
    print("task %s enviada" % task)
