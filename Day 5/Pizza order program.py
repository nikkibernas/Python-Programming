#small pizza: $10
#medium pizza: is $17
#large pizza: is $25

#pepperoni for small: +2
#pepperoni for medium or large: +3

#extra cheese for any pizza: +$1

print ("Welcome to Big Booty Bitches Pizzaria!")
size = input ("What side pizza do you want? S, M, or L: ")
pepperoni = input ("Do you want pepperoni? Y or N: ")
cheese = input ("Do you want extra cheese? Y or N: ")

#SML = 0
#meat = 0
#dairy = 0

bill = 0

if size == "S" or size == "s":
    #SML = 10
    bill += 10
elif size == "M" or size == "m":
    #SML = 17
    bill += 17
elif size == "L" or size == "l":
    #SML = 25
    bill += 25

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        #meat = 2
        bill += 2
    else:
        #meat = 3
        bill += 3
else:
        #meat = 0
        bill += 0

if cheese == "Y" or cheese == "y":
     #dairy = 1
     bill += 1
else: 
     #dairy = 0
     bill += 0

#cost = SML + meat + dairy

#print (f"Your total comes to: ${cost}")
print (f"Your bill comes to: ${bill}")