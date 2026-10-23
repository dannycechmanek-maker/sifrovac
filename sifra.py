def zasifruj(text, posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    for znak in text:
        if znak in abeceda:
            pozice = abeceda.index(znak)
            vysledek = vysledek + abeceda[(pozice + posun) % 26]
        else:
            vysledek = vysledek + znak
    return vysledek 



def desifruj(text, posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    for znak in text:
        if znak in abeceda:
            pozice = abeceda.index(znak)
            vysledek = vysledek + abeceda[(pozice - posun) % 26]
        else:
            vysledek = vysledek + znak
    return vysledek


zprava = input("Zadej text: ")
posun = int(input("Zadej posun: "))
tajne = zasifruj(zprava, posun)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, posun))
