print ("welcome to the tip calculator!")
total = float(input ("What was the total bill? $"))
split = int(input ("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

percent = (total/100*tip)
total = (percent + total)
bills = ("{:.2f}").format(total/split)

print ("Each person should pay: " + str(bills))