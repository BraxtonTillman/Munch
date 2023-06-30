'''Munch Application MVP
v0.1
By Braxton Tillman
The purpose of Munch is to produce a dinner menu from your favorite dishes,
and produce a shopping list of ingredients required.'''

#---------Imports---------------
from random import choice

# --------Functions-------------

def endingDialogue():
    print()
    print("You got it! Bye for now!")



def chooseDishes(days): 
    while len(myMenu) < int(days): #This loop is a condition to where the length(the amount of data in the list) is less than the answer given which is changed to an integer it will produce the condition under it
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here is your menu...")
    print()
    for dish in myMenu: # This loop is a condition to where every variable (dish) in the list (myMenu) is printed in a row rather all in one line
        print(myMenu.index(dish) + 1, dish) #index prints where the variable (dish) is at in the list and since it starts at 0 that's why there is a +1 there
    print()
    print("Mmmm my favorite dish is", choice(myMenu))

    
def buildShoppingList(): #This function checks everything that's put into the list (myMenu) is then added to the list (myShoppingList)
    myShoppingList = []
    if "Gyros" in myMenu:
        myShoppingList.append(gyros)
    if "Animal Style Cheeseburgers" in myMenu:
        myShoppingList.append(animalStyleCheeseburgers)
    if "Chicken Fried Rice" in myMenu:
        myShoppingList.append(chickenFriedRice)
    if "Quesadillas" in myMenu:
        myShoppingList.append(quesadillas)
    if "Spam Musubi" in myMenu:
        myShoppingList.append(spamMusubi)
    if "California Burrito" in myMenu:
        myShoppingList.append(californiaBurrito)
    if "Chorizo Burrito" in myMenu:
        myShoppingList.append(chorizoBurrito)
    if "Classic Burrito" in myMenu:
        myShoppingList.append(classicBurrito)
    if "Braxton's Breakfast" in myMenu:
        myShoppingList.append(braxtonsBreakfast)
    if "Chicken Alfredo" in myMenu:
        myShoppingList.append(chickenAlfredo)
    if "Carne Asada Fries" in myMenu:
        myShoppingList.append(carneAsadaFries)
    print()
    for dish in myShoppingList: #This conditional prints everything in the list (myShoppingList) in a row rather than all on one line.
        for ing in dish:
            print(ing)
    print()
    print("Here's your list! Hope you enjoy it!")
    

# ---------Lists-----------------

foodWeLike = ["Gyros","Animal Style Cheeseburgers","Chicken Fried Rice","Quesadillas","Spam Musubi","California Burrito","Carne Asada Fries","Chorizo Burrito","Classic Burrito","Braxton's Breakfast","Chicken Alfredo"]

gyros = ["Gyro Meat","Pita Bread","Tzatziki Sauce","French Fries","Raw Onion","Romaine Lettuce"]
animalStyleCheeseburgers = ["Ground Beef","Buns","Raw Onion","Cheese","French Fries","Mayonnaise","Mustard","White Vinegar","Ketchup","Sweet Relish","Sugar","Salt","Pepper"]
chickenFriedRice = ["Chicken Breast","Vegetable Fried Rice","Raw Onion","Jalapenos","Yum Yum Sauce","Bao Buns"]
quesadillas = ["Chicken or Steak","Raw Onion","Cheese","Chipolte Sauce","Tortilla"]
spamMusubi = ["Lite Spam","Hoisin Sauce","Soy Sauce","Honey","Rice Vinegar","White Rice","Furikake","Egg"]
californiaBurrito = ["Carne Asada","Sour Cream","Cheese","French Fries","Guac","Tortilla"]
carneAsadaFries = ["Carne Asada", "Guac","Salsa","Sour Cream","Cheese","French Fries"]
chorizoBurrito = ["Chorizo","Cheese","Egg","Tots","Salsa","Jalapenos","Raw Onion","Bacon","Tortilla"]
classicBurrito = ["Chicken or Steak","Cheese","Salsa","Peppers","Lime","Cilantro","Beans","Rice","Jalapenos","Raw Onion","Sour Cream"]
braxtonsBreakfast = ["Egg","Bacon","Hashbrown","Ketchup","Bread"]
chickenAlfredo = ["Chicken","Alfredo Sauce","Fettuccine or Rigatoni"]

myMenu = []

# How many days to plan

print("Hello, I'm Munch and I'll help you plan your dinner menu...")

answer = input("How many days would you like this plan? ")

print("Okay, I am going to plan " + answer + " dinner(s) for you.")

# Choose Dishes

chooseDishes(answer)

#Produce shopping list from dishes selected




while True:
    answer = input("Would you like a shopping list for this menu?(Use y for yes and n for no) ")
    if answer in ("y","Y","n","N"):
        break
    print("Sorry I didn't catch that. Please try again...")

if answer in ("y", "Y"):
    buildShoppingList()
else:
    endingDialogue()
    
    

    


        









