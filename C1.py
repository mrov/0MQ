# coding=utf-8
import zmq
import time
import re


# Faz a requisição para o lookup
def GetAdress(name):
    json_msg = {"type": "GET", "route": "Adress/", "name": name}
    lookup_socket.send_json(json_msg)
    msg = lookup_socket.recv_json()
    print msg['code']
    del msg['code']
    return msg


def AdressFromList(name):
    for adress in adresses:
        if adress['name'] == name:
            return adress['Adress']


# Basico do 0MQ
context = zmq.Context()
lookup_socket = context.socket(zmq.REQ)
# Conectar ao lookup
lookup_socket.connect("tcp://localhost:5555")
# Listas Usadas no programa
adresses = []
tasks_A = []
tasks_B = []


# Pede os endereços e salva em adresses
adresses.append(GetAdress("A"))
time.sleep(1)
adresses.append(GetAdress("B"))
time.sleep(1)
print(adresses)

# Le o arquivo de tarefas e separa elas para cada tipo uma lista
file = open("tasks.txt", "r")
for line in file:
    first_char = line[0]
    if first_char == "A":
        tasks_A.append(int(line[2:]))
    elif first_char == "B":
        tasks_B.append(int(line[2:]))

print("Tasks A: %s " % tasks_A)
print("Tasks B: %s " % tasks_B)
time.sleep(1)

# Conecta no A, envia as tasks assim que o A estiver pronto para recebe-las
A_socket = context.socket(zmq.REQ)
A_socket.connect(AdressFromList("A"))
json_msg = {"Tasks": tasks_A}
A_socket.send_json(json_msg)
A_msg = A_socket.recv_json()
print A_msg['code']
time.sleep(1)

# Conecta no B, envia as tasks assim que o B estiver pronto para recebe-las
B_socket = context.socket(zmq.REQ)
B_socket.connect(AdressFromList("B"))
json_msg = {"Tasks": tasks_B}
B_socket.send_json(json_msg)
B_msg = B_socket.recv_json()
print B_msg['code']
time.sleep(1)


# push_context = zmq.Context()
# push_socket = push_context.socket(zmq.PUSH)
# push_socket.bind("tcp://localhost:5558")
