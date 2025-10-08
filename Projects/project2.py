salt_points = 0
sweet_points = 0


answer = input("if you were eating ice cream and you had to pick a flavor would you pick A salted caramel or B cotton candy?")
if answer == "A"or answer == "a":
	salt_points += 1
elif answer == "B" or answer == "b":
	sweet_points += 1


answer = input("would you rather eat A sour patch kids or B goldfish crackers?")
if answer == "A"or answer == "a":
	sweet_points += 1
elif answer == "B" or answer == "b":
	salt_points += 1

answer = input("if you were at a baseball game with your friends and you guys where getting food, would you rather get A pretzel and a hotdog or B a waffle and ice cream?")
if answer == "A" or answer == "a":
	salt_points += 1
elif answer == "B" or answer == "b":
	sweet_points += 1

answer = input("would you rather have A Pringles or B a kit kat")
if answer == "A" or answer == "a" and salt_points > 2:
	print("you really like salt")
	salt_points += 1
elif answer == "B"or answer == "b":
	sweet_points += 1

answer = input("would you rather eat A a ham and cheese sandwich or B a peanut butter and jelly sandwich?")
if answer == "A" or answer == "a":
	salt_points += 1
elif answer == "B" or answer == "b":
	sweet_points += 1

if salt_points > sweet_points:
	print("You prefer salty over sweet")
elif sweet_points > salt_points:
	print("You prefer sweet over salty")
