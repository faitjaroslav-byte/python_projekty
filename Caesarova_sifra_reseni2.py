def sifrovani (text, posun):
    zasifrovany_text=""
    for znak in text:
        pismeno=ord(znak)
        posunute_pismeno = (pismeno - ord("A") + posun) % 26 + ord("A")
        zasifrovany_text+=chr(posunute_pismeno)
    return zasifrovany_text


def desifrovani (text, posun):
    desifrovany_text=""
    for znak in text:
        pismeno=ord(znak)
        posunute_pismeno = (pismeno - ord("A") - posun) % 26 + ord("A")
        desifrovany_text+=chr(posunute_pismeno)
    return desifrovany_text

text = input("Zadejte text k zašifrování:")
posun = int(input("Zadejte posun:"))
sifrovani(text,posun)
zasifrovany_text = sifrovani(text, posun)
print(zasifrovany_text)
print(desifrovani(zasifrovany_text, posun))