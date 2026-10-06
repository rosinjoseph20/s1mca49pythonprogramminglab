num=[]
n=int(input("enter the number of elements:"))
print("enter the list of intergers:")
for i in range(1,n+1):
    e=int(input())
    if(e>100):
        num.append("OVER")
    else:
        num.append(e)
print("entered list:",num)
