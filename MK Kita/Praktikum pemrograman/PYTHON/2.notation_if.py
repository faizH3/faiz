t = input('input time format: ')
time = float(t)
if time>=0 and time<=12:
  print('good morning')
elif time>=13 and time<=16:
  print('good afternoon')
elif time>=17 and time<=20:
  print('good evening')
elif time>=21 and time<=24:
  print('good night')
else:
  print('wrong input!')
