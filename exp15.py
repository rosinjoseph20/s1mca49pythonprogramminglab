c1=set()
c2=set()
n1=int(input("enter the number of colors in list1:"))
print("enter the colors to list1:")
for x in range(n1):
    color=input()
    c1.add(color)
n2=int(input("enter the number of colors in list2:"))
print("enter the colors to list2:")
for x in range(n2):
    color=input()
    c2.add(color)
diff=c1.difference(c2)
print("COLORS IN LIST1 NOT IN LIST2:",diff)
