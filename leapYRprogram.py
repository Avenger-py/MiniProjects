year=int(input("Enter year: "))
if year%100 :
    if year%400:
        print("This is a leap year")
else:
    if year%4:
        print("This is a leap year")
print("This is not a leap year")

