str1=input("Enter string:")
if len(str1)>2:
    for i in str1:
       a = str1[0:2] + str1[-2:]
    print(a)
    exit()
else:
    print(str1)
exit()
