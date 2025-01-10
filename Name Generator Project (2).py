#Name Generator

#Main
def name_generator():   #This function generates a name based on the selections the player chooses to do.
    print("Welcome to Name Generator! ")
    print("Please answer the following questions to find out your random name! ")

    ans = input("Indoors (i) or outdoors (o)? ")    #asks for input of the player
    if ans == "i":      #options if the player uses "i" then the follwoing will be shown
        ans = input("Sweet (sw) or savory (sa)? ")
        if ans == "sw":
            ans = input("Light (lt) or dark (dk)? ")
            if ans == "lt":
                print("Your name is Strawberry Shortcake!")
            else:
                print("Your name is Chocolate Mousse!")
        elif ans == "sa":
            ans = input("Soft (s) or crunchy (c)? ")
            if ans == "s":
                print("Your name is Pretzel Lord!")
            else:
                print("Your name is Chips Master!")
    if ans == "o":
        ans = input("Beach (b) or Forest (f)? ")
        if ans == "b":
            ans = input("Sunset (ss) or Sunrise (sr)? ")
            if ans == "ss":
                print("Your name is Mango Sunset!")
            else:
                print("Your name is Strawberry Blossom!")
        elif ans == "f":
            ans = input("Darkness (d) or light (l)? ")
            if ans == "d":
                print("Your name is Blueberry Storm!")
            else:
                print("Your name is Green Apple Rise!")

#main
name_generator()
