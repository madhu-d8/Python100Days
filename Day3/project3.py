print('welcome to tresure island.')
print("your mission is to find the tresure.")
choice1 = input('you\`re at a crossroad,where do you want to go? '
                'type "left" or "right".\n').lower()
if choice1 == 'left':
    choice2 = input('you\'ve came to a lake.'
                    'there is an island in the middle of the lake. '
                    'type "wait" to wait for a boat. '
                    'type "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        choice3 = input("you arrive at the island unharmed. "
                        "there is house with 3 doors. one red,"
                        "one yellow and one blue. "
                        "which colour do you choose?\n").lower()
        if choice3 == 'red':
            print("it's a room full of fire. Game over")
        elif choice3 == 'yellow':
            print("you found the tresure. you win")
        elif choice3 == 'blue':
            print("you enter a room of beasts. Game over.")
        else:
            print("you choose a door that doesn't exist. Game over")
    else:
        print("you got attacked by an angry trout. Game over.")
else:
    print("you fell into hole. Gameover.")




