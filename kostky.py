from random import randrange

cislo = randrange(1, 7)


print("Hází hráč 1:")
pocitadlo1 = 1
while cislo != 6:
    print(cislo)
    pocitadlo1 += 1
    cislo = randrange(1, 7)
print(6)


print("Počet hodů hráče 1: ", pocitadlo1)

cislo = randrange(1, 7)
print("Hází hráč 2:")
pocitadlo2 = 1
while cislo != 6:
    print(cislo)
    pocitadlo2 += 1
    cislo = randrange(1, 7)
print(6)

print("Počet hodů hráče 2: ", pocitadlo2)

cislo = randrange(1, 7)
print("Hází hráč 3:")
pocitadlo3 = 1
while cislo != 6:
    print(cislo)
    pocitadlo3 += 1
    cislo = randrange(1, 7)
print(6)

print("Počet hodů hráče 3: ", pocitadlo3)

cislo = randrange(1, 7)
print("Hází hráč 4:")
pocitadlo4 = 1
while cislo != 6:
    print(cislo)
    pocitadlo4 += 1
    cislo = randrange(1, 7)
print(6)

print("Počet hodů hráče 4: ", pocitadlo4)

seznam = pocitadlo1, pocitadlo2, pocitadlo3, pocitadlo4

seznam = sorted(seznam, reverse = True)


if seznam[0] == pocitadlo1:
    print("Vítězem je hráč číslo 1!")
elif seznam[0] == pocitadlo2:
    print("Vítězem je hráč číslo 2!")
elif seznam[0] == pocitadlo3:
    print("Vítězem je hráč číslo 3!")
elif seznam[0] == pocitadlo4:
    print("Vítězem je hráč číslo 4!")
