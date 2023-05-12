tipus=""
loero=0
ar=0
class Motor:
        def __init__(self,tipus,loero,ar):
                self.tipus=oszlop[0]
                self.loero=oszlop[1]
                self.ar=oszlop[2]
motorlista=[]
fajl=open("motor.txt","r",encoding="utf-8")
for sor in fajl:
        sor=sor.strip()
        oszlopok=sor.split(";")
        print(oszlopok[0],oszlopok[1],oszlopok[2])
print("-------------------")
