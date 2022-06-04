l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
print("NEGATIVE NUMBERS ARE : ")
for i in range(0,len(t)):
    if(t[i]<0):
        print(t[i])
