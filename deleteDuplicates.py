def noDuplicates():
    listLength=int(input("Enter length of list: "))
    L=[]
    l=[]
    while len(L)<listLength:
        a=int(input("Enter a number: "))
        L.append(a)
    for x in range(min(L),max(L)+1):
        if x in L:
            l.append(x)
    print(l)
    
        
            
            


    
