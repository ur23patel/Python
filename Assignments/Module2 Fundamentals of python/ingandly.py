str = input("Enter String : ")
if len(str) < 3:
  print(str)
elif str[-3:] == 'ing':
  print(str + 'ly')
else:
  print(str + 'ing')
