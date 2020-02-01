'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
string = str(input("Enter a string:"))
a=len(string)
b=0
if a%2==0:
    while b<(len(string)/2):
            if string[b]!=string[a-1]:
                print("Not a palindrome string")
                break
            a=a-1
            b=b+1
    else:
        print("Its a palindrome string")
else:
    while b<((len(string)-1)/2):
            if string[b]!=string[a-1]:
                print("Not a palindrome string")
                break
            a=a-1
            b=b+1
    else:
        print("Its a palindrome string")
        
        
        
    
    
