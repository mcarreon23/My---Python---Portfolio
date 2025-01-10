#Marianne Carreon
#4th Period
#11/19/24

#Init
#Function
def add(num1, num2):        #functions thats adds two numbers
    result=num1 + num2
    print("The result is: " + str(result))
def minus(num1,num2):       #functions that subtracts two numbers
    result= num1-num2
    print("The result is: " + str(result))
def times(num1,num2):   #function that multiplies two numbers
    result=num1*num2
    print("The result is: " + str(result))
def divide(num1,num2):      #function that divides two numbers
    result=num1/num2
    print("The result is: " + str(result))

def simplecalculator():     # this function calculates in multiplication,divison,addition,and subtration of any numbers that the player chooses to input.
    print("Welcome Preschooler to Simple Calculator!")
    while True:     #the function is looped.
        print("Please choose and operation: ")
        print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit """)
        operation = int(input("(1-5):"))
        if operation == 1:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            add(add1,add2)
        if operation == 2:
            minus1=int(input("Enter first number:"))
            minus2=int(input("Enter second number: "))
            minus(minus1,minus2)
        if operation == 3:
            times1=int(input("Enter the first number: "))
            times2=int(input("Enter the second number: "))
            times(times1,times2)
        if operation == 4:
            divide1=int(input("Enter the first number:"))
            divide2=int(input("Enter the second number:"))
            divide(divide1,divide2)
        if operation == 5:
            print("Thank You for using Simple Calculator. Goodbye")
            break

#Main
simplecalculator()




