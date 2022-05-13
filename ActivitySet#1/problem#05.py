# Functions
hrs = input("Enter Hours:")
h=int(hrs)
rate=input("enter the rate for per hour:")
r=float(rate)
def computepay(h, r):
    if h<=40:
        pay=h*r
    else:
        s=h-40
        pay=40*r+1.5*s*r
    return pay

p = computepay(h, r)
print("Pay", p)