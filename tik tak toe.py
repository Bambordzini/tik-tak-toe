print("""
  
         __________ ___  _______
         |________| |  | |   __|
            |  |    |  | |  |      
            |  |    |  | |  |                  
            |__|    |__| |_____|       ___________   _________   _________
  _________  _______   _____           |         |  |   ___   | |   _____|
  |________| _____  | |  __|           |_________|  |  |   |  | |  |___
    |  |   | |___|  | | |                 |   |     |  |___|  | |  ____|
    |  |   |  ___   | | |___              |   |     |         | |  |_____
    |__|   |__|  |__| |_____|             |___|     |_________| |_________|     """)
print()
print()
print("1. Rozpocznij nową grę")
print("2. Poznaj zasady gry")
print("3. Wyjdź z programu")
print()

tablica = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

rows = ["a", "b", "c"]
kolumny = [1, 2, 3]
uzyte_pola = []
wolne_pole = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

def print_tablica():
    print("    1   2   3")
    for i in range(len(tablica)):
        print(rows[i], end="  ")
        print("  ".join(tablica[i]))

def sprawdz(gracz):
    for row in tablica:
        if row.count(gracz) == 3:
            return True
    for i in range(len(kolumny)):
        if tablica[0][i] == gracz and tablica[1][i] == gracz and tablica[2][i] == gracz:
            return True
    if tablica[0][0] == gracz and tablica[1][1] == gracz and tablica[2][2] == gracz:
        return True
    if tablica[0][2] == gracz and tablica[1][1] == gracz and tablica[2][0] == gracz:
        return True
    return False

print_tablica()

while True:
    wybor = input("Wybierz opcję (1, 2 lub 3, aby wyjść): ")
    if wybor == "1":
        print_tablica()
        gracz = "x"
        while True:
            punkt = input(f"Gracz {gracz.upper()}, wybierz pole np. c2 ")
            if punkt not in wolne_pole:
                print("Niepoprawne pole")
            else:
                uzyte_pola.append(punkt)
                wolne_pole.remove(punkt)
                row = rows.index(punkt[0])
                kolumna = kolumny.index(int(punkt[1]))
                tablica[row][kolumna] = gracz
                print_tablica()
                if sprawdz(gracz):
                    print(f"Gracz {gracz.upper()} wygrywa")
                    break
                if "." not in [cell for row in tablica for cell in row]:
                    print("Remis!")
                    break
                if gracz == "x":
                    gracz = "o"
                else:
                    gracz = "x"
    elif wybor == "2":
        print("Gra polega na ułożeniu pionowo, poziomo lub na skos ciąg tych samych znaków x lub o gracz któremu uda się to zrobić wygrywa")
    elif wybor == "3":
        break
    else:
        print("zły wybór")

        