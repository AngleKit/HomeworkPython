import random
import turtle

def SadTurtle(answer):
    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle.speed(15)
    turtle.pencolor('black')
    turtle.fillcolor('black')

#Left eye
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.right(90)
    turtle.right(90)
    turtle.right(90)
    turtle.circle(50)
    turtle.end_fill()

#Right eye
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(100, 50)
    turtle.pendown()
    turtle.circle(50)
    turtle.end_fill()

#Mouth
    turtle.penup()
    turtle.goto(-150, -150)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(100)

def fireworks():
#black background to look lke the night sky
    screen = turtle.Screen()
    screen.bgcolor("black")
#to increase the speed that turtle draws the fireworks
    turtle.speed(150)

#colors to use for the fireworks
    colors = ["blue", "red", "purple", "magenta", "orange", "gold"]
    random_index = int()
    x = int()
    y = int()
    for i in range(0, 10):
#random locations
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
#moving the turtle
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
#generating random firework colors
        size = random.randint(15, 200)
        random_index = random.randint(0, 5)
        pen_size = random.randint(1, 10)
        turtle.color(colors[random_index])

        for i in range(36):
            turtle.forward(size)
            turtle.backward(size)
            turtle.left(10)
#Stop turtle from crashing?

def CheckAnswer(guess, answer):
    if guess == answer:
        print("Correct!")
    return True;

    if guess != answer:
        print("Wrong! Try again")
    return False;

def GameOptions():
    #print options
        #categor choices
    print("Category Options")
    print("----------------------")
    print("Animals\nObjects\nPlaces")
    print()    

def GetCategory(choice):
    #Variables
    animals = [ "Tiger", "Bear", "Robin", "Whale"]
    objects = [ "Hat", "TV", "Phone", "Cake"]
    places = [ "Paris", "Washington DC", "New York", "Rome"]
    answer = str()

    #Choose catagory and Randomize answer
    if choice == "Animals":
        answer = random.choice(animals)
    elif choice == "Objects":
        answer = random.choice(objects)
    elif choice == "Places":
        answer = random.choice(places)
    #end if

    #return answer
    return answer
#Function for giving hints
def hints_answers(answer, attempts):
    #Hints for option: Animals
    if answer == "Tiger" and attempts == 5:
        print ("Hint: This animal is a sort of feline")

    if answer == "Tiger" and attempts == 10:
        print ("Hint: This animal is the largest type of feline")

    if answer == "Tiger" and attempts == 15:
        print ("Hint: We have a Detroit sports team named after this animal")

    if answer == "Bear" and attempts == 5:
        print ("Hint: These large animals can suprisingly climb trees")

    if answer == "Bear" and attempts == 10:
        print ("Hint:These large mammals are extremely defensive of their young ")

    if answer == "Bear" and attempts == 15:
        print ("Hint: Chicago has a sports team named after this mammal")

    if answer == "Robin" and attempts == 5:
        print ("Hint: This animal is a type of bird")

    if answer == "Robin" and attempts == 10:
        print ("Hint:These birds are mostly colored brown, red, black, white, and grey")

    if answer == "Robin" and attempts == 15:
        print ("Hint: Finish this title: The Tales of ___ Hood.")

    if answer == "Whale" and attempts == 5:
        print ("Hint: This animal lives in the ocean")

    if answer == "Whale" and attempts == 10:
        print ("Hint:These are some of the largest sea creatures")

    if answer == "Whale" and attempts == 15:
        print ("Hint: Captain Ahab in the famous book was trying to kill one of these")
    #Hints for option: Objects
    if answer == "Hat" and attempts == 5:
        print ("Hint: This article of clothing comes in differest shapes")

    if answer == "Hat" and attempts == 10:
        print ("Hint:This article of clothing is worn of the top half of your body")

    if answer == "Hat" and attempts == 15:
        print ("Hint: This article of clothing commonly represents sports teams")

    if answer == "TV" and attempts == 5:
        print ("Hint: This object provides entertainment")

    if answer == "TV" and attempts == 10:
        print ("Hint:This object comes in a variety of sizes")

    if answer == "TV" and attempts == 15:
        print ("Hint: This object is found in most living rooms")

    if answer == "Phone" and attempts == 5:
        print ("Hint: This object was less common 20+ years ago")

    if answer == "Phone" and attempts == 10:
        print ("Hint:This object used to just be in homes and businesses")

    if answer == "Phone" and attempts == 15:
        print ("Hint: This object has become significantly smaller over time")

    if answer == "Cake" and attempts == 5:
        print ("Hint: This food comes in many flavors")

    if answer == "Cake" and attempts == 10:
        print ("Hint:This food is usually served as dessert")

    if answer == "Cake" and attempts == 15:
        print ("Hint: This dessert is common on birthdays")
    #Hints for option: Places
    if answer == "Paris" and attempts == 5:
        print ("Hint: The city is in Europe")

    if answer == "Paris" and attempts == 10:
        print ("Hint:The city is in France")

    if answer == "Paris" and attempts == 15:
        print ("Hint: The city is the capital of France")

    if answer == "Washington DC" and attempts == 5:
        print ("Hint: The city is in America")

    if answer == "Washington DC" and attempts == 10:
        print ("Hint:The city is formally known as the District of Columbia")

    if answer == "Washington DC" and attempts == 15:
        print ("Hint: The city is the capital of America")

    if answer == "Rome" and attempts == 5:
        print ("Hint: The city is in Europe")

    if answer == "Rome" and attempts == 10:
        print ("Hint:The city is in Italy")

    if answer == "Rome" and attempts == 15:
        print ("Hint: This city is the capital of Italy")

    if answer == "New York" and attempts == 5:
        print ("Hint: The city is in America")

    if answer == "New York" and attempts == 10:
        print ("Hint:Central park is located in this city")

    if answer == "New York" and attempts == 15:
        print ("Hint: The empire state building is located here")
    
def main():
    #Variables
    choice = str()
    answer = str()
    guess = str()
    attempts = int()
    user_answer = str()
    user_answer = "Y"
    
    #game continue loop
    while user_answer == "Y":
        #Game options
        print("Capitalize the first letter of your answer")
        GameOptions()
        #Ask for Catagory choice
        choice = input("Please enter a Category: ")
        answer = GetCategory(choice)
        #Loop guesses
        while attempts < 20:
            hints_answers(answer, attempts)
            guess = input("Enter in your Guess: ")
            CheckAnswer(guess, answer)
            #Attempts counter
            attempts = attempts + 1
            #Checks Answer gives win/loss action
            if guess == answer:
                fireworks()
                attempts = 20
            elif guess != answer and attempts == 20:
                SadTurtle(answer)
        #turtle dance
        #Tell user anwser
        print("The answer was:\t", answer)
        #Ask if user wants to play
        print("Type capital Y or N")
        user_answer = input("Would you like to play again?: ")
        print()
        attempts = 0
        turtle.clear()
    #end while
        
main()
