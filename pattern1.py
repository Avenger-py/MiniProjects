a=int(input("Enter a number: "))
for x in range(1,a+1):
    for i in range(1,x+1):
      print(i, end=" ")
      if i==x:
            for j in range(x-1,0,-1):
                print(j, end=" ")
    print("\n")

