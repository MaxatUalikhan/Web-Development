def count_code(str):
  a=0
  for i in range(len(str)):
    if str[i:i+2]=="co"and str[i+3:i+4]=="e":
      a+=1
  return a
