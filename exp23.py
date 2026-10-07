num_list=[]
n=int(input("enter the number of valuesin list:"))
print("enter the elements")
for i in range(n):
    val=int(input())
    num_list.append(val)
total=0
for item in num_list:
    total=total+item
print("the suum of all items in the list is:",total)
    
