a=(1,2,3,4,5)
print("TUPLE WITH NUMBERS : ",a)
b=()
c=list(b)
num=int(input("ENTER TOTAL NUMBER OF TUPLE ELEMENTS : "))
for i in range(0,num):
    value=input("ENTER VALUE YOU WANTS TO ADD : ")
    c+=value
b=tuple(c)
print(b)
    