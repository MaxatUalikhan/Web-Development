def lone_sum(a, b, c):
  if a==b==c:
    return 0
  elif a==b:
    return c
  elif b==c:
    return a
  elif c==a:
    return b
  elif a!=b!=c:
    return a+b+c