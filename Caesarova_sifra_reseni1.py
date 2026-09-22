import random
import string

def sifrovani (text, posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vysledek = ""
    for znak in text:
        pozice = abeceda.index(znak)
        nova_pozice = (pozice + posun) % len(abeceda)
        vysledek += abeceda[nova_pozice]
    return vysledek
  
    print ("zašifrovaný text je: " + vysledek)

def desifrovani (text, posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vysledek = ""
    for znak in text:
        pozice = abeceda.index(znak)
        nova_pozice = (pozice - posun) % len(abeceda)
        vysledek += abeceda[nova_pozice]
    return vysledek


def testovani():
    for i in range(10):
        text = "".join(random.choices(string.ascii_uppercase, k=10))
        #print ("Testovací text: " + text)
        posun = random.randint(1, 25)
        #print ("Posun: " + str(posun))
        assert text == desifrovani(sifrovani(text, posun), posun)
    #print("Všechny testy proběhly úspěšně.")


text = input("Zadejte text k zašifrování:")
posun = int(input("Zadejte posun:"))
testovani()
sifrovani (text, posun) 
print ("zašifrovaný text je: " + sifrovani(text, posun))
print ("dešifrovaný text je: " + desifrovani(sifrovani(text, posun), posun))