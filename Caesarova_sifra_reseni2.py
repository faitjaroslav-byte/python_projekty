def sifrovani (text, posun):
    zasifrovany_text=""
    for znak in text:
        pismeno=ord(znak)
        posunute_pismeno=pismeno+posun
        zasifrovany_text+=chr(posunute_pismeno)
    print (zasifrovany_text)


def desifrovani (text, posun):
    desifrovany_text=""
    for znak in text:
        pismeno=ord(znak)
        posunute_pismeno=pismeno-posun
        desifrovany_text+=chr(posunute_pismeno)
    print (desifrovany_text)

text = input("Zadejte text k zašifrování:")
posun = int(input("Zadejte posun:"))
sifrovani(text,posun)