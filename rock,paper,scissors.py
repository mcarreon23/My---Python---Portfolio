#Marianne Carreon
#1/6/25
#Rock Paper Scissors
#init

import random

wins=0
losses=0
ties=0

#functions
def rpsgame():
    global wins
    global losses
    global ties
    print("Welcome to Rock Paper Scissors!")
    print("Pick between rock,paper or scissors and if you no longer wish to play pick end")
    while True:
        print("Select rock, paper,scissors, or end")
        player = input("Selection: ")
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("Computer choose rock")
        elif computer == 2:
            computer = "paper"
            print("Computer choose paper")
        elif computer == 3:
            computer = "scissors"
            print("Computer choose scissors")
        if player == "paper" and computer == "paper":
            ties = ties +1
            print("Tie no one gets a point")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "rock" and computer == "rock":
            ties= ties +1
            print("Tie no one gets a point")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "scissors" and computer == "scissors":
            ties= ties +1
            print("Tie no one gets a point")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "scissors" and computer == "paper":
            wins= wins +1
            print("Player won")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "scissors" and computer == "rock":
            losses= losses +1
            print("Computer won")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "paper" and computer == "rock":
            wins= wins +1
            print("Player won")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "paper" and computer == "scissors":
            losses= losses + 1
            print("Computer won")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "rock" and computer == "paper":
            losses =losses +1
            print("Computer won")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "rock" and computer == "scissors":
            wins = wins +1
            print("Player won")
            print("The score is:" + "Wins "+ str(wins)+ " Losses " + str(losses)+ " Ties "+ str(ties))
        elif player == "end":
            print("Thank you for playing Rock Paper Scissors")
            break

#main
rpsgame()
