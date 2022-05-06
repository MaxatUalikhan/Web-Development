def xor(a,b):
    if a==1 and b==1 or a==0 and b==0:
        return 0
    return 1

a,b=input().split()
a,b=int(a),int(b)
print(xor(a,b))