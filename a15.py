l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
ce=0
co=0
for i in range(0,len(t)):
    if(t[i]%2==0):
        ce+=1
    else:
        co+=1
print("TOTAL EVEN NUMBERS ARE : ",ce)
print("TOTAL ODD NUMBERS ARE : ",co)