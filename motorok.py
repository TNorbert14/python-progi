class Motor:
        def __init__(self,sor):
                oszlop=sor.strip().split(";")
                self.nev=oszlop[0]
                self.ar=int(oszlop[1])

fajl=open("motor.txt","r",encoding="utf-8")
motor_lista=[Motor(sor) for sor in fajl]
for motor in motor_lista:
        print(motor.nev,motor.ar)
print("---------------------------------")

print(f"Motorok Száma: {len(motor_lista)} db")

print("---------------------------------")

print("13.000.000Ft feletti motorok:")
for motor in motor_lista:
        if motor.ar>13000000:
                print("\t"+motor.nev)

motor_szam=0
for motor in motor_lista:
        if motor.ar>13000000:
                motor_szam+=1
print(f"13.000.000 FT feletti motorok száma: {motor_szam} db")

print("-----------------------------------")

sorba=sorted(motor_lista, key=lambda n: n.ar)
print(f"A legdrágább növény: {sorba[-1].nev}")