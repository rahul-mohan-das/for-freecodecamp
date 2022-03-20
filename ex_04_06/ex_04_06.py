def computepay(hours,rate):
    if(hours>40):
        totalPay=40*rate+((hours-40)*1.5*rate)
    else:
        totalPay=hours*rate
    return totalPay
xh=input("Enter Hours:")
xr=input("Enter Rate:")
fh=float(xh)
fr=float(xr)
xp=computepay(fh,fr)
print("Pay:",xp)
