x=int(input("enter the value1:"))
y=int(input("enter the value2:"))
for z in range(x,y):
  for i in range(x,y-z):
    print("*",end=" ")
  print("\r")
