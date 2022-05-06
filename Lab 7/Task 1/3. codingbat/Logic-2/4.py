def no_teen_sum(a,b,c):
    d=(a,b,c)
    return sum(fix_teen(i) for i in d)
def fix_teen(n):
    return 0 if n not in (15,16) and 13<=n<=19 else n