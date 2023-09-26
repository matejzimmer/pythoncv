od = {}
spatne = 0
dobre = 0
print("Vítejte v matematickém dotazníku")
print("Dostanete 5 otázek, zkuste odpovědět co nejlépe!")

# První otázka
prvni = input("1. Kolik je 12/2*(1+2)? ")
od["Prvni otazka"] = prvni
if int(prvni) != 15:
    spatne += 1
else:
    dobre += 1

# Druhá otázka
druhy = input("2. 9*N se rovná 108. Co je N? ")
od["Druha otazka"] = druhy
if int(druhy) != 12:
    spatne += 1
else:
    dobre += 1

# Třetí otázka
treti = input("3. Hodnota cos 360°? ")
od["Treti otazka"] = treti
if int(treti) != 1:
    spatne += 1
else:
    dobre += 1

# Čtvrtá otázka
ctvrty = input("4. Kolik hran má osmistěn? ")
od["Ctvrta otazka"] = ctvrty
if int(ctvrty) != 8:
    spatne += 1
else:
    dobre += 1

# Pátá otázka
paty = input("5. Kolik stupňů je polovina pravého úhlu? ")
od["Pata otazka"] = paty
if int(paty) != 45:
    spatne += 1
else:
    dobre += 1

print("Děkujeme za vaše odpovědi")
for otazka, odpoved in od.items():
    print(f"{otazka}: {odpoved}")

print(f"Špatně: {spatne}, Dobře: {dobre}")