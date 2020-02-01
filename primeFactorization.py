def prime():
    a=int(input("Enter a number: "))
    b=2
    while a>1:
        if a%b==0:
            print("{}".format(b))
            a=a/b
            continue
        b=b+1
