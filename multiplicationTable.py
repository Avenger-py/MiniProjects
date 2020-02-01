a=int(input("Enter a number you want the multiplication table for: "))
b=int(input("Enter a number upto which you want the multiplication table: "))
c=1
while (c!=b+1) :
      print("{} x {} = {}". format(a,c,a*c))
      c=c+1
print("----------")
