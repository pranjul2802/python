a=input("Enter the first string-   ")
b=input("Enter the second string-   ")
c=[]
len=len(a)
for i in range(0,len):
    if (a[i] not in c):
        c.append(a[i])
for j in c:
    b=b.replace(j,"")
print(b)