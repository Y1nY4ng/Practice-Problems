groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

for grocery in groceries: 
    y = input("What do you want removed from the list? ")

    if y in groceries:
        groceries.remove(y)
        print(groceries)
    elif y == "stop":
        print(groceries)
        break
    else:
        print("Sorry, I don't understand?")

