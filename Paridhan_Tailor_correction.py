#!usr/bin/python
from datetime import datetime, time, date, timedelta
print("Paridhan Tailor")

def Paridhan_Tailor(Serial_No,Bill_No,Name,Mobile_No,Address,DOO, DateOfOrder, Load_Time,DOD,Invoice):
    Serial_No = 2
    Bill_No = 125
    Name = "Pradumn Parihar"
    Mobile_No = 123456789
    Address = "Motibanala,Colony"
    DOO = datetime.now()
    DateOfOrder = DOO.strftime('%Y-%m-%d')
    Load_Time = datetime.now()
    td = timedelta(days=4)
    DOD = DOO+td  
    Invoice = 750
    print("Serial_No:",Serial_No,"\nBill_No:",Bill_No,"\nName:",Name,"\nMobile_No:",Mobile_No,"\nAddress:",Address,"\nDOO:",DateOfOrder,"\nLoad_Time:",Load_Time,"\nDOD:",DOD,"\nInvoice:",Invoice)
    return
Paridhan_Tailor("Serial_No","Bill_No","Name","Mobile_No","Address","DOO","DateOfOrder","Load_Time","DOD","Invoice")
