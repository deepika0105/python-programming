even=[]
odd=[]
x=int(input("enter the value1:"))
y=int(input("enter the value2:"))
for z in range(x,y):
  if(z%2==0):
    even.append(z)
  else:
    odd.append(z)
print("even",even)   
print("odd",odd) 