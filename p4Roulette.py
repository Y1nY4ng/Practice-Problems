import random 
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    spaces = generate_wheel()

    money = 1000

    while True:
        print("you have $ " + str(money))

        bet = int(input("how much do you want to bet? "))
        color = input("What color do you want to bet on? ")

        print("The wheel is spinning....")
        time.sleep(2)

        landed = spin_wheel(spaces)

        print("It landed on " + landed)
        if color == landed:
            money = money + bet
            print("Congrats! You now have $" + str(money))
        else:
            money = money - bet
            print("Sorry! You now have $" + str(money))
    
        play_again = input("Do you want to play again? ")
        if play_again == "no":
            break

play_game()