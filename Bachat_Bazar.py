#!usr/bin/python
from datetime import datetime,date,time,timedelta

print("Bachat_Bazar")

def Bachat_Bazar(S_No,Bill_No,Name,Phone,Address,DOO,Load_time,DOD,Invoice):
    S_No = 1
    Bill_No = 201
    Name = "Hemant Parihar"
    Phone = 2233456987
    Address = "Apni Duniya Mai,Mast"
    DOO = datetime.now()
    Load_time = datetime.now()
    DO = timedelta(days=3)
    DOD = DOO+DO 
    Invoice = 920
    print("S_No:-",S_No,"\nBill_No:-",Bill_No,"\nName:-",Name,"\nPhone:-",Phone,"\nAddress:-",Address,"\nDOO:-",DOO,"\nLoad_time:-",Load_time,"\nDOD:-",DOD,"\nInvoice:-",Invoice)
    return

Bachat_Bazar("S_No","Bill_No","Name","Phone","Address","DOO","Load_time","DOD","Invoice")


    
    
    
    

