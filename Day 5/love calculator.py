print ("Welcome to the love calculator!")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

letter_T = name1.count("t") + name2.count("t")
letter_R = name1.count("r") + name2.count("r")
letter_U = name1.count("u") + name2.count("u")
letter_E = name1.count("e") + name2.count("e")

letter_L = name1.count("l") + name2.count("l")
letter_O = name1.count("o") + name2.count("o")
letter_V = name1.count("v") + name2.count("v")
letter_E = name1.count("e") + name2.count("e")

truecount = str(letter_T + letter_R + letter_U + letter_E)
lovecount = str(letter_L + letter_O + letter_V + letter_E)

score = (truecount + lovecount)

if score <= "10" or score >= "90":
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score >= "40" and score <= "50":
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score comes to: {score}")