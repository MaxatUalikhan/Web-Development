n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(1,n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        b+=1
print(b)