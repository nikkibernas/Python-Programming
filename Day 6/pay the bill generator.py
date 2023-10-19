
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

num_items = len(names)

random_choice = random.randint (0, num_items -1)

person_who_pays = names[random_choice]

print (f"the person who is going to pay is, {person_who_pays}")