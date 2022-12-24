#!/usr/bin/python

import sys
import os
import time
import random


slp_time = int(sys.argv[1])
pid = os.getpid()
ppid = os.getppid()

print(f"Child [{pid}]: I am started. PID {pid}. Parent PID {ppid}")
time.sleep(slp_time)
print(f"Child [{pid}]: I am ended. PID {pid}. Parent PID {ppid}")

exit_status = random.randint(0, 1)
sys.exit(exit_status)