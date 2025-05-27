def kalkulacka():
    print("=== Jednoduchá kalkulačka ===")
    try:
        cislo1 = float(input("Zadej první číslo: "))
        operace = input("Zadej operaci (+, -, *, /): ")
        cislo2 = float(input("Zadej druhé číslo: "))

        if operace == "+":
            vysledek = cislo1 + cislo2
        elif operace == "-":
            vysledek = cislo1 - cislo2
        elif operace == "*":
            vysledek = cislo1 * cislo2
        elif operace == "/":
            if cislo2 != 0:
                vysledek = cislo1 / cislo2
            else:
                print("Chyba: dělení nulou!")
                return
        else:
            print("Neplatná operace!")
            return

        print(f"Výsledek: {vysledek}")
    except ValueError:
        print("Zadej platná čísla!")

kalkulacka()
