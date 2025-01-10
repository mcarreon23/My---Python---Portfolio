#Marianne Carreon
#Multiplication Quiz
#1/8/24
#Init
import random

#Functions
def test():
    global correct
    print("Welcome to Multiplication Facts! Enter the answer to the following problems! ")
    level = input("What level would you like to do? hard (h) , meduium (m) , or  easy (e)") #asks the user to choose a level
    correct = 0     #number of questions correct
    if level == "e":
        print("You choose the easy level.")
        for i in range (5) :
            num1= random.randint(0,6)      #selects one number randomly
            num2= random.randint(0,6)       #selects a second number randomly
            facts= num1 * num2
            print("What is " + str(num1)+ "x" + str(num2))       # asks the multiplication fact
            answer= input("Your answer is : ")      # ask the user for an answer
            if str(facts) == str(answer):    #checks if the answer that the user entered is correct
                correct = correct + 1
                print("Correct")
            elif str(facts) != str(answer):
                print("Incorrect")
    elif level == "m" :
        print("You choose the medium level")
        for i in range (5) :
            num1= random.randint(7,11)      #selects one number randomly  middle numbers not too hard
            num2= random.randint(7,11)       #selects a second number randomly
            facts= num1 * num2
            print("What is " + str(num1)+ "x" + str(num2))       # asks the multiplication fact
            answer= input("Your answer is : ")      # ask the user for an answer
            if str(facts) == str(answer):        #checks if the answer that the user entered is correct
                correct = correct + 1
                print("Correct")
            elif str(facts) != str(answer):
                print("Incorrect")
    elif level == "h":
        print("You choose level hard.")
        for i in range (5) :
            num1= random.randint(12,16)      #selects one number randomly
            num2= random.randint(12,16)       #selects a second number randomly
            facts= num1 * num2
            print("What is " + str(num1)+ "x" + str(num2))       # asks the multiplication fact
            answer= input("Your answer is : ")      # ask the user for an answer
            if str(facts) == str(answer):        #checks if the answer that the user entered is correct
                correct = correct + 1
                print("Correct")
            elif str(facts) != str(answer): #checks if the facts answer and the input is incorrect it will print incorrect
                print("Incorrect")

    print("Your final score is " + str(correct)+"/5.")
#main
test()
