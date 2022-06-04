l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
x=t[::-1]
print("ORIGNAL TUPLE IS : ",t)
print("REVERSED TUPLE IS : ",x)