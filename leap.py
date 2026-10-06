y1=2026
y2=int(input("enter the year:"))
print("leap year between",y1,"and",y2,"are")
for i in range(y1,y2+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        print(i,"")
