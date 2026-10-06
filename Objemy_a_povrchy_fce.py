import math


def nacti_cislo(popis):
	"""Načte číslo a přijímá desetinnou tečku i čárku."""
	return float(input(popis).replace(",", "."))


def spocitej_krychli():
	a = nacti_cislo("Délka hrany a: ")
	return "krychle", 6 * a**2, a**3


def spocitej_kvadr():
	a = nacti_cislo("Délka a: ")
	b = nacti_cislo("Šířka b: ")
	c = nacti_cislo("Výška c: ")
	return "kvádr", 2 * (a * b + a * c + b * c), a * b * c


def spocitej_valec():
	r = nacti_cislo("Poloměr podstavy r: ")
	v = nacti_cislo("Výška v: ")
	return "válec", 2 * math.pi * r * (r + v), math.pi * r**2 * v


def spocitej_kouli():
	r = nacti_cislo("Poloměr r: ")
	return "koule", 4 * math.pi * r**2, (4 / 3) * math.pi * r**3


def zobraz_menu():
	print("\nVyber těleso:")
	print("1 – Krychle")
	print("2 – Kvádr")
	print("3 – Válec")
	print("4 – Koule")


def zobraz_vysledky(nazev, povrch, objem):
	print(f"\nVýsledky pro těleso – {nazev}:")
	print(f"Povrch: {povrch:.2f}")
	print(f"Objem:  {objem:.2f}")


def zpracuj_volbu(volba):
	funkce = {
		"1": spocitej_krychli,
		"2": spocitej_kvadr,
		"3": spocitej_valec,
		"4": spocitej_kouli,
	}
	if volba not in funkce:
		print("Neplatná volba. Vyber číslo od 1 do 4.")
		return

	nazev, povrch, objem = funkce[volba]()
	zobraz_vysledky(nazev, povrch, objem)


def main():
	pokracovat = "ano"
	while pokracovat in ("ano", "a", "jo", "j"):
		zobraz_menu()
		volba = input("Zadej číslo volby (1–4): ").strip()
		zpracuj_volbu(volba)
		pokracovat = input("\nChceš počítat další těleso? (ano/ne): ").strip().lower()
	print("Program byl ukončen.")


#if __name__ == "__main__":
main()
