l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
sum=0
for i in range(0,len(t)):
    sum+=t[i]
print("SUM OF TUPLE ITEMS IS : ",sum)