def factorial(a):
    b=1
    for x in range(1,a+1):
        b=b*x
    print("{}!={}".format(a,b))

def factorial2(a):
    b=1
    x=1
    while x<=a:
        b=b*x
        x=x+1
    print("{}!={}".format(a,b))
        
     
