def zasifruj(text, posun):
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    return text


def desifruj(text, posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    for znak in text:
        pozice = abeceda.index(znak)
        vysledek = vysledek + abeceda[pozice - posun]
    return vysledek


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))
