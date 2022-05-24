#!usr/bin/python
print("Defining a Function")

'''
def Liquid(Acid, handwash,c ):
    Acid = 5
    handwash = 45
    c = Acid+handwash
    print (Acid,handwash, c)
    return


Liquid("acid", "dettol","Total")
#Liquid(Acid, handwash,c)
'''
'''
def Bachatbazar(soap,detergent,liquid,powder,dio):
    soap = 30
    detergent = 25
    liquid = 24
    powder = 12
    dio = 22
    print("soap",soap,"\ndetergent",detergent,"\nliquid",liquid,"\npowder",powder,"\ndio",dio)
    return

Bachatbazar("soap","detergent","liquid","powder","dio")
'''

def Bachatbazar(soap,detergent,liquid,powder,dio):
    soap = 30
    detergent = 25
    liquid = 24
    powder = 12
    dio = 22
    print("soap",soap,"\ndetergent",detergent,"\nliquid",liquid,"\npowder",powder,"\ndio",dio)
    return

Bachatbazar("soap","detergent","liquid","powder","dio")
'''
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
'''

def changeme(Mlist):
    Mlist.append([20,30,4])
    print(Mlist)
    return

klist = [50,10,85]
changeme(klist)


    


