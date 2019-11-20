choice=input("add/sub/mul/div")
a=input()
b=input()
if "." in a and b:
  x=float(a)
  y=float(b)
  print(a,b)
elif a.isalpha() and b.isalpha():
    print("enter only numbers") 
else:
  x=int(a)
  y=int(b)
if choice=="add":
    print(x+y)
elif choice=="sub":
    print(x-y)
elif choice=="mul":
    print(x*y)
else:
    print(x/y)