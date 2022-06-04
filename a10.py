a=(3,6,1,4,7,8,2,10,5,9)
max=0
min=a[0]
for i in range(0,len(a)):
    if(a[i]>max):
        max=a[i]
    if(a[i]<min):
        min=a[i]
print("LARGEST NUMBER IS : ",max)
print("SMALLEST NUMBER IS : ",min)