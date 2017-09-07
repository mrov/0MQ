# coding=utf-8
import zmq
import time

# Worker B conecta ao B
context = zmq.Context()
B_worker_receive = context.socket(zmq.PULL)
B_worker_receive.connect("tcp://127.0.0.1:5560")
# Envia para o Sink
B_worker_send = context.socket(zmq.PUSH)
B_worker_send.connect("tcp://127.0.0.1:5561")
print("Woker B Ready!")

while True:
    task = B_worker_receive.recv_json()
    print("dormir %s" % task['task'])
    time.sleep(int(task['task']))
    B_worker_send.send_json({"done": 1})
    print("job done B")
