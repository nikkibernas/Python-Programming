print ("Welcome to the rollar coaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print ("You can ride the rollar coaster!")
    age = int(input ("How old are you? "))
    if age <= 12:
        print ("You must pay $5 since you're 12 or under.")
    elif age >= 18:
        print ("You must pay $15 since you're 18 or older.")
    else:
        print ("you must pay $12 since youre between the ages of 12 to 18.")
else:
    print ("Sorry but you are too short to ride.")