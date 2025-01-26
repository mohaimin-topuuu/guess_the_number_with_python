import random 

target = random.randint(1, 100)

while True: 
    userChoice = input("GUESS the target or type Quit to quit the game: ")
    if (userChoice == "quit" or userChoice == "Quit" or userChoice == "QUIT"):
        print("Thank you for playing")
        break
    userChoice = int(userChoice)

    if (userChoice == target):
        print("Congratulations, you guessed correctly!")
    elif (userChoice < target):
        print("Too low, try again!")
    else: 
        print("Too high, try again!")
print("Game over!")


        