l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
print(t)
sume=0
sumo=0
for i in range(0,len(t)):
    if(t[i]%2==0):
        sume+=t[i]
    else:
        sumo+=t[i]
print("SUM OF EVEN DIGITS ARE : ",sume)
print("SUM OF ODD DIGITS ARE",sumo)
