import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while(guess!=random_number):
        guess=int(input(f"guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry,Guess again. Too low.")
        elif guess > random_number:
            print("Sorry,Guess again. Too high.")
     
    print("Kahoot! Guessed Right")
x=int(input("enter ending range:"))    
guess(x)

