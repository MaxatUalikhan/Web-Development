x=int(input())
count=0
i=1
while i*i<x:
    if x%i==0:
        count=count+2
    i=i+1
if i*i==x: 
    count=count+1
print(count)