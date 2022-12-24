#!/usr/bin/python

import os
import sys
import random


def create_ch():
    ch = os.fork()
    if ch == 0:
        argument = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", argument)
    print(f"Parent [{os.getpid()}]: I ran children process with PID {ch}")


num_ch = sys.argv[1]
num_ch = int(num_ch)

for i in range(0, num_ch):
    create_ch()

while num_ch > 0:
    child_pid, status = os.wait()
    status = status / 256
    status = int(status)
    print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")
    if status == 0:
        num_ch = num_ch - 1
    else:
        create_ch()