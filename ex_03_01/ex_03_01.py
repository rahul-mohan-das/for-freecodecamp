xh=input("Enter Hours:")
xr=input("Enter Rate:")
fh=float(xh)
fr=float(xr)
print("Hours:",fh)
print("Rate:",fr)
if(fh>40):
    totalPay=40*fr+((fh-40)*1.5*fr)
    print("Overtime")
else:
    totalPay=fh*fr
    print("Regular")
print("Total pay:",totalPay)
