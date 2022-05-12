# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter the rate per hour:")
r= float(rate)
if h<=40:
    pay= h*r
    print(pay)
else:
    s=h-40    
    pay = h*r+0.5*r*s
    print(pay)



#conditional execution 3.3
score = input("Enter Score between 0.0 and 1.0: ")
s= float(score)
if 0.0<=s<=1.0:
    if s>=0.9:
        print('A')
    elif s>=0.8:
        print('B')
    elif s>=0.7:
        print('C')
    elif s>=0.6:
        print('D')
    elif s<0.6:
        print('F')
else:
    print("the number entered is out of range")
