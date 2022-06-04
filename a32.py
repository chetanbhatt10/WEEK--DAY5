import math
a=float(input("ENTER COMMON : "))
c=int(input("ENTER DIFFERENT SIDE : "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-a)*(s-c))
print("AREA OF ISOSCELES TRIANGLE IS : ",area)