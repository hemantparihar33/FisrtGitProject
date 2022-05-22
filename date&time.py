#!usr/bin/python

print("date&time")

import time;

time = time.localtime(time.time())
print("Current Time",time)

import time;
samay = time.asctime(time.localtime(time.time()))
print("Formatted Time",samay)
