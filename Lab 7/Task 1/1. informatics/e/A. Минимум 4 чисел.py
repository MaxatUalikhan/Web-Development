def min4(a):
    b=0
    for i in range(4):
        if i==0:
            b=a[i]
        elif a[i]<b:
            b=a[i]
    return b        

a=list(map(int,input().split()))
print(min4(a))