#Developed by: Anya Liu
#Date: Feb 8, 2023
#Desc: A program to assign each invitee the user inputs a meal depending on their diet preferences. The program also shows the total costs, the total cost after tax, and the total cost after tipping

#assign variables for each meal option which also stores their prices
totalLasagna = 32.50
totalFishFillet = 38.99
totalCaesarSalad = 34.99
totalSteak = 40.60
totalBeverage = 9.99

#variables to determine if the invitees have specific diets
yesKetoFriendly = True
yesVeganMeal = True
yesGlutenFree = True

#counters to count the amount of invitees ordering each meal
pizzaCount = pastaCount=falafelCount=steakCount=beverageCount= 0

#have the user input a positive integer to indicate the number of invitees they want
noOfInvitees = int(input("Please enter the number of invitees: "))

#loop through the invitees with a for loop. use if statements to see which diets each invitee has to ultimately determine which meal they would be assigned
for i in range (1, noOfInvitees + 1):
    print("Please enter the order details for invitee Number %d / %d" % (i, noOfInvitees))

    ketoFriendly = input("Do you want a keto friendly meal?")
    if ketoFriendly == 'y':
        yesKetoFriendly = True
    else:
        yesKetoFriendly = False

    veganMeal = input("Do you want a vegan meal?")
    if veganMeal == 'y':
        yesVeganMeal = True
    else:
        yesVeganMeal = False

    gultenFree = input("Do you want a Gluten-free meal?")
    if gultenFree == 'y':
        yesGlutenFree = True
    else:
        yesGlutenFree = False

    if yesVeganMeal and not yesKetoFriendly and not yesGlutenFree:
        pastaCount = pastaCount + 1
    elif yesKetoFriendly and yesVeganMeal and yesGlutenFree:
        falafelCount = falafelCount + 1
    elif yesKetoFriendly and yesVeganMeal and not yesGlutenFree:
        pizzaCount = pizzaCount + 1
    elif yesKetoFriendly and yesGlutenFree and not yesVeganMeal:
        steakCount = steakCount + 1
    elif not yesKetoFriendly and not yesGlutenFree and not yesVeganMeal:
        beverageCount = beverageCount + 1
#end loop

#user inputs amount to tip
amountToTip = int(input("How much do you want to tip your server (% percent)?"))

#output the number of each meal and their total cost
print("You have %d invitees with the following orders:" % noOfInvitees)
print("%d invitees ordered Pizza. The cost is: $%.2f" % (pizzaCount, pizzaCount * totalPizza))
print("%d invitees ordered Pasta. The cost is: $%.2f" % (pastaCount, pastaCount * totalPasta))
print("%d invitees ordered Falafel. The cost is: $%.2f" % (falafelCount, falafelCount * totalFalafel))
print("%d invitees ordered Steak. The cost is: $%.2f" % (steakCount, steakCount * totalSteak))
print("%d invitees ordered only beverage. The cost is: $%.2f" % (beverageCount, beverageCount * totalBeverage))

#calculations for the total cost and the total cost after tax
totalCost = totalPizza+totalPasta+totalFalafel+totalSteak+totalBeverage
totalAfterTax = (totalCost * 0.13)+totalCost

#outputs for the total cost, the total cost after tax, and the total after the tipping
print("The total cost before tax is $%.2f" % totalCost)
print("The total cost after tax is $%.2f" % totalAfterTax)
print("The total cost after " + str(amountToTip) + "% tip is $" + str(round(totalAfterTax * ((100 + amountToTip)/100))))