class Motor:
    def __init__(self,tipus,loero,ar):
        self.tipus=tipus
        self.loero=loero
        self.ar=ar
motorlista=[]
fajl=open("motor.txt","r",encoding="utf-8")
for sor in fajl:
    sor=oszlop().strip().split(;)
print(motorlista)
print("A lista hossza: "+len(motorlista))
sorba=sorted(motorlista key=lambda k:k.ar)
print("10 legdrágább motor: "+motorlista)