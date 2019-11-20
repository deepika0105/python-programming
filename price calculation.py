user=input("name")
phno=int(input("phno"))
emailid=input("emailid")
print("bike=rs10/km,car=rs30/km,auto=rs20/km:")
choice=input("bike/car/auto:")
price1=10
price2=30
price3=20
print("source:0 to destination:100 km only")
source=int(input("source"))
destination=int(input("destination"))
if  source=="-" and destination=="-":
    print("enter valid:")
elif source=="0" and destination=="0":
    print("enter valid:")       
elif destination<source:
    totalkm=source-destination
    print(totalkm)       
else:
    totalkm=destination-source
    print(totalkm)      
if choice=="bike":
    amount=totalkm*price1
    print(amount,user,phno,emailid)
elif choice=="car":
    amount1=totalkm*price2
    print(amount1,user,phno,emailid)
else:
    amount2=totalkm*price3
    print(amount2,user,phno,emailid)
