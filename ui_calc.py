import tkinter as tk
from tkinter import messagebox

def spocitej():
    try:
        cislo1 = float(vstup1.get())
        cislo2 = float(vstup2.get())
        operace = operace_var.get()

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
                messagebox.showerror("Chyba", "Dělení nulou!")
                return
        else:
            messagebox.showerror("Chyba", "Neplatná operace!")
            return

        vysledek_label.config(text=f"Výsledek: {vysledek}")
    except ValueError:
        messagebox.showerror("Chyba", "Zadej platná čísla!")

# Okno
okno = tk.Tk()
okno.title("Grafická kalkulačka")

# Vstupy
tk.Label(okno, text="První číslo:").grid(row=0, column=0)
vstup1 = tk.Entry(okno)
vstup1.grid(row=0, column=1)

tk.Label(okno, text="Druhé číslo:").grid(row=1, column=0)
vstup2 = tk.Entry(okno)
vstup2.grid(row=1, column=1)

# Operace
tk.Label(okno, text="Operace:").grid(row=2, column=0)
operace_var = tk.StringVar(okno)
operace_var.set("+")
operace_menu = tk.OptionMenu(okno, operace_var, "+", "-", "*", "/")
operace_menu.grid(row=2, column=1)

# Tlačítko a výsledek
spocitej_btn = tk.Button(okno, text="Spočítej", command=spocitej)
spocitej_btn.grid(row=3, column=0, columnspan=2)

vysledek_label = tk.Label(okno, text="Výsledek: ")
vysledek_label.grid(row=4, column=0, columnspan=2)

okno.mainloop()
