n=int(input("Enter a number: "))
d=2
while n>1:
    if n%d==0:
        n=n/d
        continue
    d=d+1
print( "Greatest prime factor of this number is {}".format(d))
