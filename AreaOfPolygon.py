def polygon():
    q=input("Are number of sides of polygon finite? (y/n): ")
    s=float()
    pi=3.141592
    if q=="y":
        a=int(input("Enter number of sides of polygon: "))
        if a==0 or a==1 or a==2 or a>4:
            print("Am i a joke to you?")
        else:
            if a==3:
               print("Enter the sides: \n")
               b=float(input("First side: "))
               c=float(input("Second side: "))
               d=float(input("Third side: "))
               if b+c>d and c+d>b and b+d>c:
                   s=(b+c+d)/2
                   print("Area = {}".format((s*(s-b)*(s-c)*(s-d))**0.5))
               else:
                   print("This triangle cannot exist")
            if a==4:
                print("Enter the sides: \n")
                B=float(input("First side: "))
                C=float(input("Second side: "))
                D=float(input("Third side: "))
                E=float(input("Fourth side: "))
                if B==D and C==E:
                    print("Area = {}".format(B*D))
                else:
                    print("Coming Soon!")

    else:
        print("Its a cicle LOL.\n")
        r=float(input("Now enter the radius: "))
        print("Area = {}".format(pi*(r**2)))
    
    

                

            
    
            
        
    
       
    
