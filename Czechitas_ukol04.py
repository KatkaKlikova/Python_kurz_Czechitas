'''První funkce ověří telefonní číslo. 
Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. 
Uživatel platí 3 Kč za každých započatých 180 znaků.'''

def telefon(cislo:str):
    #cislo = str(cislo)
    cislo = cislo.replace(" ", "")
    if len(cislo) == 13:
        if cislo[0:4] == "+420" and cislo[1:].isdigit():
            kontrola = True
        else:
            kontrola = False
    elif len(cislo) == 9 and cislo.isdigit():
        kontrola = True
    else:
        kontrola = False
    return kontrola

def cena(zprava):
    zprava = str(zprava)
    delka = len(zprava)
    krok = delka // 180
    castka = krok * 3
    return castka

print("Napište telefonní číslo: ")
telefonni_cislo = input()

kontrola = telefon(telefonni_cislo)
if not kontrola:
    print("Telefonní číslo má nesprávný formát (+420......... / .........).") 
if kontrola:
    print(f"Napište text zprávy: ")
    castka = cena(input())
    print(f"Celková cenaje {castka} Kč.")
    