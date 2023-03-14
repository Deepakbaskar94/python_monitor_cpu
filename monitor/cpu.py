#!/usr/bin/env python
import psutil
# gives a single float value
cpu = psutil.cpu_percent()
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary 
dictvm = dict(psutil.virtual_memory()._asdict())

for key in dictvm.keys():
    value = dictvm[key]
    gb = value/(1024 * 1024 * 1024)
    dictvm[key] = gb
    print(key + ":" + str(dictvm[key]))

# keysList = list(dictvm.keys())
# print("keylist: ", keysList)


# you can have the percentage of used RAM
psutil.virtual_memory().percent
# 79.2
# you can calculate percentage of available memory
memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
# 20.8

print("cpu: ", cpu)
# print("dictvm: ", dictvm)
print("memory: ", memory)