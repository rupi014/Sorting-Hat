
gry = 0
rav = 0
huf = 0
sly = 0

print(""" Do you like Dawn or Dusk?

1. Dawn
2. Dusk 
          """)


dawn_dusk = int(input("Your response: "))

if dawn_dusk == 1:
  gry += 1
  rav += 1
elif dawn_dusk == 2:
  huf += 1
  sly += 1
else:
  print("Wrong answer")

print()

print("""When I'm dead, I want people to remember me as: 

1. The Good
2. The Great
3. The Wise
4. The Bold
""")

dead_quest = int(input("Your response: "))

if dead_quest == 1:
  huf += 2
elif dead_quest == 2:
  sly += 2
elif dead_quest == 3:
  rav += 2
elif dead_quest == 4: 
  gry += 2
else:
  print("Worng answer")

print()

print("""Which kind of instrument most pleases your ear?

1. The Violin
2. The Trumpet
3. The Piano
4. The Drum
""")


instrument_quest = int(input("Your response: "))

if instrument_quest == 1:
  sly += 4
elif instrument_quest == 2:
  huf += 4
elif instrument_quest == 3:
  rav += 4
elif instrument_quest == 4: 
  gry += 4
else:
  print("Worng answer")

houses = {"Gryffindor": gry, "Ravenclaw": rav, "Hufflepuff": huf, "Slytherin": sly}

selected_house = max(houses, key=houses.get)

print()

print(f"Your house is {selected_house}")