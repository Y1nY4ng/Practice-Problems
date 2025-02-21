import random

random_num = random.randint(0,100)
x = 0
while True:   
    guess = int(input("guess a number \n"))
    if guess > random_num:
        print("guess lower")
        x += 1
    elif guess < random_num:
        print("guess higher")
        x += 1
    else:
        x += 1
        y = str(x)
        print("You got it right! You took: " + y + " tries.")

        break