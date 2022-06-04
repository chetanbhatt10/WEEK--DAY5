l=[]
num=int(input("ENTER TOTAL NUMBER OF ELEMENT NEEDED : "))
for i in range(0,num):
    value=int(input("ENTER NUMBER : "))
    l.append(value)
t=tuple(l)
cntp=0
cntn=0
for i in range(0,len(t)):
    if(t[i]>0):
        cntp=cntp+1
    else:
        cntn=cntn+1
print("COUNT OF POSITIVE NUMBERS ARE: ",cntp)
print("COUNT OF NEGATIVE NUMBERS ARE : ",cntn)