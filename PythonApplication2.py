heroes=["Заяц","Волк","Медведь","Лиса"]

for hero in heroes:
    print(f"{hero}:Колобок, я тебя съем!")
    if hero=="Лиса":
        print("Koлобок спел песенеку и попался Лисе.Его съели!")
    break
else:
    print("Колобок: Я от тебя уйду!")
