def alarm_clock(day, vacation):
  if day<=5 and day>=1:
    if vacation==False:
      return '7:00'
    return '10:00'
  elif vacation==True:
    return 'off'
  return '10:00'