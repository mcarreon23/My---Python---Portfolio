#Marianne Carreon
#4th period
#12/10/24
#Init
import random      
#Functions
print("""Welcome to MadLibs!
    Enter words that follow the category that is being asked.
    At the end you will have your own personalized short story!""")
def mad_lib():      #This functions creates three different types of short stories with the users input of the questions asked.
     adjective= input("Please enter a adjective : ")
     place = input("Please enter a location : " )
     person1 = input("Please enter a person's name : ")
     food = input("Please enter a food: ")
     objective = input ("Please enter an objective : ")
     emotion = input ("Please enter an emotion : ")
     person2 = input("Please enter another person's name : ")
     outcome= random.randint(1,3)
     if outcome == 1 :
          print(" One day there was someone named " + str(person1) + " who was " + str(adjective) +
          " and wanted to " + str(objective) + " at " + str(place) +  " with " + str(person2) +
          ". They decided to go get " + str(food) +  " When they finished eating, they felt " + str(emotion) + ".")
     if outcome == 2:
          print("There once was a person named " + str(person1) + " and they had a sibling named " + str(person2) +
               ". They both loved to go to " + str(place) + " to " + str(objective) + " but always had mixed feeling, sometimes they felt " +
               str(emotion) + ". Whenever they went to " + str(place) + " they ate " + str(food) +
               " and then when the sun set they went home.")
     if outcome == 3 :
          print("Someone by the name of " + str(person1) + " who was " + str(adjective) + " liked to go to " + str(place)+ "." + " They met up with " +
          str(person2) + " and they ate " + str(food)+ "." + " They liked to go there because they knew they could " + str(objective)+
          "." + " Sometimes when they were in " + str(place) + " they felt " + str(emotion)+ " but spening time together was overly fun either way.")


#Main
mad_lib()
