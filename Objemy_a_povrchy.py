import math


# Program počítá povrch a objem vybraného tělesa.
pokracovat = "ano"

while pokracovat in ("ano", "a", "jo", "j"):
	print("\nVyber těleso:")
	print("1 – Krychle")
	print("2 – Kvádr")
	print("3 – Válec")
	print("4 – Koule")
	volba = input("Zadej číslo volby (1–4): ").strip()

	if volba == "1":
		# Krychle má šest stejných čtvercových stěn.
		a = float(input("Délka hrany a: ").replace(",", "."))
		povrch = 6 * a**2
		objem = a**3
		nazev = "krychle"
	elif volba == "2":
		# Povrch kvádru tvoří tři dvojice shodných obdélníků.
		a = float(input("Délka a: ").replace(",", "."))
		b = float(input("Šířka b: ").replace(",", "."))
		c = float(input("Výška c: ").replace(",", "."))
		povrch = 2 * (a * b + a * c + b * c)
		objem = a * b * c
		nazev = "kvádr"
	elif volba == "3":
		# Pi je dostupné v modulu math.
		r = float(input("Poloměr podstavy r: ").replace(",", "."))
		v = float(input("Výška v: ").replace(",", "."))
		povrch = 2 * math.pi * r * (r + v)
		objem = math.pi * r**2 * v
		nazev = "válec"
	elif volba == "4":
		r = float(input("Poloměr r: ").replace(",", "."))
		povrch = 4 * math.pi * r**2
		objem = (4 / 3) * math.pi * r**3
		nazev = "koule"
	else:
		print("Neplatná volba. Vyber číslo od 1 do 4.")
		povrch = None

	if povrch is not None:
		# Výsledky zobrazíme zaokrouhlené na dvě desetinná místa.
		print(f"\nVýsledky pro těleso – {nazev}:")
		print(f"Povrch: {povrch:.2f}")
		print(f"Objem:  {objem:.2f}")

	pokracovat = input("\nChceš počítat další těleso? (ano/ne): ").strip().lower()

print("Program byl ukončen.")
