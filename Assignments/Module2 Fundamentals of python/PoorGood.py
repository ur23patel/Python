str1=input("Enter String : ")
snot = str1.find("not")
sbad = str1.find("poor")

if sbad > snot:
    str1 = str1.replace(str1[snot:(sbad + 4)],"good")
print(str1)
    
