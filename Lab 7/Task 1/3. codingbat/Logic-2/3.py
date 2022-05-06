def lucky_sum(a, b, c):
  d=[a,b,c]
  e=0
  for i in d:
    if i==13:
      return e
    e+=i
  return e