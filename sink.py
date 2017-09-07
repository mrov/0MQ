# coding=utf-8
import zmq
import time

context = zmq.Context()
sink_socket = context.socket(zmq.PULL)
sink_socket.bind("tcp://127.0.0.1:5561")
completed_tasks = 0
started = False
start = 0
print("Sink Ready!")

while True:
    result = sink_socket.recv_json()
    if (not started):
        start = time.time()
        started = True
    if result['done'] == 1:
        completed_tasks += 1
    if completed_tasks == 10:
        complete_time = time.time() - start
        print("JOB DONE IN %s SECONDS" % complete_time)
