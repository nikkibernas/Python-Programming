print ("Welcome to the roller coaster!")
height = int(input("what is your height in cm? "))
cost = 0

if height >= 120:
    print ("You can ride the roller coaster!")
    age = int(input ("How old are you? "))
    if age <= 12:
        cost = 5
        print ("Your ticket is $5 since you're under 13.")
    elif age <= 18:
        cost = 12
        print ("Your ticket is $12 since you're under 19.")
    elif age <= 55 and age >= 45:
        cost = 0    
    else:
        cost = 15
        print ("Your ticket is $15 since you're over 19 and not in a midlife crisis.")
else:
    print ("Sorry but you are too short to ride.")

photo = int(input("Do you want a photo with your ticket for an additional $3? Type 1 for yes and 2 for no: "))
if photo == 1:
    if cost == 0:
        print ("Thank you, due to you being in a midlife crisis, all fees have been waivered.")
    else: 
        total = cost + 3
        print (f"Thank you, your total comes to: ${total}")
elif cost == 0:
    print ("Thank you, due to you being in a midlife crisis, all fees have been waivered.")
else:
    print (f"Thank you, your total comes to ${cost}")