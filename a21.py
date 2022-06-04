l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
min=t[0]
for i in range(0,len(t)):
    if(t[i]<min):
        min=t[i]
print("MINIMUM ELEMENT IS : ",min)