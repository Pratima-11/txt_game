def start_game():
    print("Welcome, adventurer!")
    print("You find yourself at the entrance of a dark forest. Will you enter?")
    
    choice1 = input("Type 'yes' to enter, or 'no' to stay out: ").lower()
    
    if choice1 == 'yes':
        print("\nYou step into the forest. The trees are tall and ancient, and it's eerily quiet.")
        print("After walking for a while, you come to a fork in the path.")
        
        choice2 = input("Do you go 'left' or 'right'?: ").lower()
        
        if choice2 == 'left':
            print("\nYou take the left path and soon reach a sparkling river.")
            print("There's a small boat tied to the shore.")
            
            choice3 = input("Do you 'cross' the river or 'follow' it along the shore?: ").lower()
            
            if choice3 == 'cross':
                print("\nYou row across the river safely and find a hidden treasure chest!")
                print("Congratulations, you've found the treasure!")
            else:
                print("\nYou follow the river, but soon it gets dark, and you lose your way.")
                print("You wander aimlessly until morning, exhausted. Game over.")
        
        elif choice2 == 'right':
            print("\nYou take the right path and soon hear strange noises.")
            print("A wild beast jumps out and attacks!")
            print("You try to fight, but you are overpowered. Game over.")
        
        else:
            print("\nThat's not a valid direction. You stand still until nightfall. Game over.")
    
    elif choice1 == 'no':
        print("\nYou decide not to enter the forest. Perhaps another adventure awaits another day.")
        print("Game over.")
    
    else:
        print("\nInvalid choice. Please start the game again and follow the instructions.")

start_game()