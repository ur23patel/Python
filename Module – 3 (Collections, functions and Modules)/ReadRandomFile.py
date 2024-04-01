import random

file=open("tops1.txt","w")
file.write("This is file management demo using python.\n")
file.write("Hello World\n")
file.write("Urvi Patel\n")
file.write("Lived in USA\n")
file.close()
print("File written Successfully")
print("************************************************************************")


file=open("tops1.txt","r")
lines = file.readlines()
print(random.choice(lines))
file.close()
print("************************************************************************")
