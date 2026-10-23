def zasifruj(text, posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"

    vysledek = ""

    for znak in text:

        pozice = abeceda.index(znak)

        vysledek = vysledek + abeceda[(pozice + posun) % 26]

    return vysledek
 



def desifruj(text, posun):
    # TODO (B): posuň každé písmeno o 'posun' míst dozadu
    return text


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))
