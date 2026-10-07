result=[]
start=int(input("enter starting range:"))
end=int(input("enter ending number:"))
for num in range(start,end):
    r=int(num**0.5)
    if r*r==num:
        if all(int(d)%2==0 for d in str(num)):
            result.append(num)
print("four digit even perfect squares:")
print(result)
