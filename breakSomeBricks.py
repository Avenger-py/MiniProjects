t=int(input())
while t!=0:
    s,w1,w2,w3=map(int,input().split())
    if s>=(w1+w2+w3):
       print(1)
    elif s>=(w1+w2) or s>=(w2+w3):
       print(2)
    else:
       print(3)
    t=t-1
     
 
