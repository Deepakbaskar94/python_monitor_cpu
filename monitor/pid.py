# https://iq.opengenus.org/cpu-and-ram-usage-python/

import psutil
import os

# my_process = psutil.Process(getpid())
# print("Name:", my_process.name())
# print("PID:", my_process.pid)
# print("Executable:", my_process.exe())
# print("CPU%:", my_process.cpu_percent(interval=1))
# print("MEM%:", my_process.memory_percent())



# Imports

# size = os.get_terminal_size()

for process in [psutil.Process(pid) for pid in psutil.pids()]:
    try:
        name = process.name()
        mem = process.memory_percent()
        cpu = process.cpu_percent(interval=0.1)
        pid = process.pid
        exe = process.exe()
    except psutil.NoSuchProcess as e:
        print(e.pid, "killed before analysis")
    else:
        print("Name:", name)
        print("CPU%:", cpu)
        print("MEM%:", mem)
        print("PID:", pid)
        print("Executable:", exe)
    print("-" * os.get_terminal_size().lines)