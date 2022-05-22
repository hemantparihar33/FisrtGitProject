#!usr/bin/python

print("Calendar")

import time;

time = time.asctime(time.localtime(time.time()))
print(time)


import calendar;
calendar = calendar.month(2022,1)
print(calendar)
