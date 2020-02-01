#the function "fibonnaci(n)" gives nth term of the series
def fibonnaci(n):   #n is the number of terms of the fibonnaci series
    if n<0:
        print("Enter a valid value for n")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def Terms(terms):
    for x in range(1,terms+1):
       print(fibonnaci(x))

def Sum(n):
    s=0
    while n!=0:
        sum=sum+fibonnaci(n)
        n=n-1
    print(sum)

def evensum(n):
    S=0
    for x in range(1,n+1):
        if fibonnaci(x)%2==0:
            S=S+fibonnaci(x)
    print(S)
            
    


    



