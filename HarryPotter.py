# Harry Potter Sorting Hat Quiz
houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

# Q1
print('Q1) Do you prefer Dawn or Dusk?\n 1) Dawn\n 2) Dusk')
answer = int(input('Enter your answer (1-2): '))
if answer == 1:
    houses["Gryffindor"] += 3  
elif answer == 2:
    houses["Hufflepuff"] += 2  
else:
    print('Wrong input')

# Q2
print("Q2) When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")
answer = int(input('Enter your answer (1-4): '))
if answer == 1:
    houses["Hufflepuff"] += 3
elif answer == 2:
    houses["Slytherin"] += 4
elif answer == 3:
    houses["Ravenclaw"] += 3
elif answer == 4:
    houses["Gryffindor"] += 4
else:
    print('Wrong input')

# Q3
print('Q3) Which kind of instrument most pleases your ear?\n1) The Violin\n2) The Trumpet\n3) The Piano\n4) The Drum')
answer = int(input('Enter your answer (1-4): '))
if answer == 1:
    houses["Slytherin"] += 2
elif answer == 2:
    houses["Hufflepuff"] += 3
elif answer == 3:
    houses["Ravenclaw"] += 4
elif answer == 4:
    houses["Gryffindor"] += 5
else:
    print('Wrong input')

for house, points in houses.items():
    print(f"{house}: {points}")

chosen_house = max(houses, key=houses.get)
print(f"\n🎉 Your house is: {chosen_house}!")
