
pisen = """Ať mír dál zůstává s touto krajinou.

Zloba, závist, zášt, strach a svár,
ty ať pominou, ať už pominou.
Teď když tvá ztracená vláda věcí tvých
zpět se k tobě navrátí, lide, navrátí.


Z oblohy mrak zvolna odplouvá
a každý sklízí setbu svou.
Modlitba má ta ať promlouvá k srdcím,
která zloby čas nespálil
jak květy mráz, jak mráz.

Ať mír dál zůstává s touto krajinou.

Zloba, závist, zášt, strach a svár,
ty ať pominou, ať už pominou.
Teď když tvá ztracená vláda věcí tvých
zpět se k tobě navrátí, lide, navrátí."""

pocet = 0
for i in range(0, len(pisen) - 1):
    if pisen[i] == "k" or pisen[i] == "K":
        pocet = pocet + 1

print("Počet 'k' je: ", pocet)
