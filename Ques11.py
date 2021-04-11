a=str(input('Enter your string\n'))
b=a.split()
c=[]
for i in b:
    if(i not in c):
        c.append(i)
st1=' '
print(st1.join(c))