import random
import string
import tkinter as tk

def sifrovani (text, posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vysledek = ""
    for znak in text:
        if znak in abeceda:
            pozice = abeceda.index(znak)
            nova_pozice = (pozice + posun) % len(abeceda)
            vysledek += abeceda[nova_pozice]
        else:
            vysledek += znak
    return vysledek

    print ("zašifrovaný text je: " + vysledek)

def desifrovani (text, posun):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vysledek = ""
    for znak in text:
        if znak in abeceda:
            pozice = abeceda.index(znak)
            nova_pozice = (pozice - posun) % len(abeceda)
            vysledek += abeceda[nova_pozice]
        else:
            vysledek += znak
    return vysledek

def zasifrovat():
    text = vstup.get("1.0", tk.END).strip().upper()
    posun = int(pole_posun.get())
    zasifrovany_text = sifrovani(text, posun)
    vystup.delete("1.0", tk.END)
    vystup.insert(tk.END, zasifrovany_text)

def testovani():
    for i in range(10):
        text = "".join(random.choices(string.ascii_uppercase, k=10))
        #print ("Testovací text: " + text)
        posun = random.randint(1, 25)
        #print ("Posun: " + str(posun))
        assert text == desifrovani(sifrovani(text, posun), posun)
    #print("Všechny testy proběhly úspěšně.")

### inicializace GUI
okno = tk.Tk()
okno.title("Caesarova šifra")
okno.geometry("700x300")

#### popisky
popisek_vstup = tk.Label(okno, text="Text:")
popisek_vstup.grid(row=0, column=0, padx=10, pady=10)
popisek_vystup = tk.Label(okno, text="Zašifrovaný text:")   
popisek_vystup.grid(row=0, column=1, padx=10, pady=10)

### textová pole
vstup=tk.Text(okno, height=5, width=30)
vstup.grid(row=1, column=0, padx=10, pady=10)
vystup=tk.Text(okno, height=5, width=30)
vystup.grid(row=1, column=1, padx=10, pady=10)

popisek_posun = tk.Label(okno, text="Posun:")
popisek_posun.grid(row=2, column=0, padx=10, pady=10)
pole_posun = tk.Entry(okno)
pole_posun.grid(row=2, column=1, padx=10, pady=10)
pole_posun.insert(0, "3")

tlacitko_zasifrovat = tk.Button(okno, text="Zašifrovat", command=zasifrovat)
tlacitko_zasifrovat.grid(row=3, column=0, padx=10, pady=10)
okno.mainloop()