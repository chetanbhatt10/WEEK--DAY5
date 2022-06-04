a=(1,2,3,4,5,6,7,8,9,10)
item=int(input("ENTER ITEM YOU WANTS TO CHECK : "))
for i in range(0,len(a)):
    if(a[i]==item):
        print("FOUND")
        break
        