# coding=utf-8
import zmq
import time

# Worker A conecta ao A
context = zmq.Context()
A_worker_receive = context.socket(zmq.PULL)
A_worker_receive.connect("tcp://127.0.0.1:5559")
# Envia para o Sink
A_worker_send = context.socket(zmq.PUSH)
A_worker_send.connect("tcp://127.0.0.1:5561")
print("Woker A Ready!")

while True:
    task = A_worker_receive.recv_json()
    print("dormir %s" % task['task'])
    time.sleep(int(task['task']))
    A_worker_send.send_json({"done": 1})
    print("job done A")
