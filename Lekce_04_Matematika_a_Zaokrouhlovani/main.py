# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:cislo = int(input("Zadej číslo: "))
cislo += 10
print("Výsledek:", cislo)


# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
na_osobu = celkem / lidi
print("Každý zaplatí:", round(na_osobu, 2), "Kč")



# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
# plocha = 3.14 * r * r
# Sem doplň kód:r = float(input("Zadej poloměr: "))
plocha = 3.14 * r * r
print("Plocha kruhu:", round(plocha))
