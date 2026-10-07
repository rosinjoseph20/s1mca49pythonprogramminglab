c=int(input("how many elements:"))
list=[]
for i in range(c):
    list.append(int(input("enter the element:")))
    list=[i for i in list if i%2!=0]
print(list)
