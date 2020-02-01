#Chef decided to write an infinite sequence. Initially, he wrote 0, and then he started repeating the following process:

#Look at the last element written so far (the l-th element if the sequence has length l so far); let's denote it by x.
#If x does not occur anywhere earlier in the sequence, the next element in the sequence is 0.
#Otherwise, look at the previous occurrence of x in the sequence, i.e. the k-th element, where k<l, this element is equal to x and all elements between the k+1-th and l−1-th are different from x. The next element is l−k, i.e. the distance between the last two occurrences of x.
#The resulting sequence is (0,0,1,0,2,0,2,2,1,…):
def s(x):
    n=x-2
    if x==1:
        return 0
    elif x==2:
        return 0
    elif x>2:
        while n>0:
            if s(x-1)==s(n):
                print((x-1)-n)
                break
            n=n-1
    else:
        print(0)
def find(x,n):
    count=0
    while n>0:
        if x==s(n):
            count=count+1
        n=n-1
    print(count)
    
        
                
                
                
