a=input()
b=''
c=0
d=0
for i in a:
    b=i+b
for i in b:
    d=d+int(i)*2**c
    c=c+1
print(d)