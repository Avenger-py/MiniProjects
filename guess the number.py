a=2
b=0
c=str()
count=0
print("Welcome to this game, do you want to play?")
while b!=a:
    c=str(input(""))
    if c=="Exit":
        print("You have left this game")
        break
    else:
        b=int(input("Guess a number from 1 to 10: "))
        if a-b>=4 and a>b:
            print("Too low!")
        elif a-b<4 and a>b:
            print("Close!")
        elif b-a<4 and b>a:
            print("Close!")
        elif b-a>=4 and b>a:
            print("Too high!")
        count=count+1
else:
    print("You guessed it right!")
print("Number of guesses:{}".format(count))

