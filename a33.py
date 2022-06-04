import math
a=float(input("ENTER 1st SIDE: "))
b=float(input("ENTER 2nd SIDE : "))
c=int(input("ENTER 3rd SIDE : "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("AREA OF TRIANGLE IS : ",area)