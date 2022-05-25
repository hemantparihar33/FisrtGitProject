#!usr/bin/python

print("funtion")

def Car(Tyre,Miroor,Ac,Player,Sunroof):
    Tyre = 4
    Miroor = 2
    Ac = 4
    Player = 1
    Sunroof  = 1
    print("Tyre",Tyre,"\nMiroor",Miroor,"\nAc",Ac,"\nPlayer",Player,"\nSunroof",Sunroof)
    return

Car("Tyre","Miroor","Ac","Player","Sunroof")

def Car_part(warrenty):
    warrenty.append(['2 Year','1 Year','3 Year','5 Year','10 year'])
    print(warrenty)
    return

warrenty = ['5 Year','20 Year','3. Year','5. Year','70 year']

Car_part(warrenty)
