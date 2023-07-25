import random

print("\nHey! are you here to play rock, paper, scissors...\n")

while True:
    rock = 0
    paper = 1
    scissor = 2

    user = int(input("Choose a number:\n \tRock -> [0]\t Paper -> [1]\t Scissor -> [2] \t"))
    computer_choice = [0, 1, 2]
    computer = random.choice(computer_choice)

    print(f"\nYour choice is {user}")
    print("\n")
    print("Now It's computer's turn .....")
    print("\n")
    print(f"Computer choose {computer}\n")
    

    if user == computer:
        print("It's a tie!\n")
    elif (user == rock & computer == scissor) | (user == paper & computer == rock) | (user == scissor & computer == paper):
        print("You won!\n")
    else:
        print("You loose!\n")
        print("Keep it up, you can do it! ^_^\n")

        print("Do you want to play again?")

        play_again = input("Press (y/n)\n")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break
    



    