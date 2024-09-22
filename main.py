soubor = "text.txt"

#napsani
with open(soubor, "w") as f:
    f.write("ahoj\n")
    f.write("ahoj2\n")

#pridani
with open(soubor, "a") as f:
    f.write("toto se pridalo\n")

with open(soubor, "a") as f:
    f.write("a toto taky")

#cteni
with open(soubor, "r") as f:
    x = f.read()
    # print(x)

#BONUS 1
with open(soubor, "r") as f:

    #pocitani slov
    z = f.read()
    y = z.split()
    pocet_slov = 0
    for slovo in y:
        pocet_slov += 1
    print(f"pocet slov je: {pocet_slov}")

    #pocitani znaku
    pocet_znaku = 0
    for znak in z:
        pocet_znaku += 1
    print(f"pocet znaku je: {pocet_znaku}")
    