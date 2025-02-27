menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def temp(item,price):
    menu[item] = price

def NewMenu():
    x = input("What do you want to add? ")
    y = input("What price should it be? ")
    temp(x,y)
    print(menu)

NewMenu()