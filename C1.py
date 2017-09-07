# coding=utf-8
import zmq
import time
import re


# Faz a requisição para o lookup
def GetAdress(name):
    json_msg = {"type": "GET", "route": "Adress/", "name": name}
    socket.send_json(json_msg)
    msg = socket.recv_json()
    print msg['code']
    del msg['code']
    return msg


# Basico do 0MQ
context = zmq.Context()
socket = context.socket(zmq.REQ)
# Conectar ao lookup
socket.connect("tcp://localhost:5555")
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
        print("Task %s Registered in %s" % (line[2:].strip('\n'), first_char))
    elif first_char == "B":
        tasks_B.append(int(line[2:]))
        print("Task %s Registered in %s" % (line[2:].strip('\n'), first_char))

print(tasks_A)
print(tasks_B)


# push_context = zmq.Context()
# push_socket = push_context.socket(zmq.PUSH)
# push_socket.bind("tcp://localhost:5558")
