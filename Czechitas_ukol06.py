'''
Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253'''

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        return "Vozidlo není k dispozici."
    
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}"

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

print("Jakou značku si přejete půjčit? Peugeot nebo Škoda?")  
prani = input()

if prani == "Škoda":
    print(Skoda.get_info())
    print(Skoda.pujc_auto())
elif prani == "Peugeot":
    print(Peugeot.get_info())
    print(Peugeot.pujc_auto())

print("Jakou značku si přejete půjčit nyní? Peugeot nebo Škoda?")  
prani = input()

if prani == "Škoda":
    print(Skoda.get_info())
    print(Skoda.pujc_auto())
elif prani == "Peugeot":
    print(Peugeot.get_info())
    print(Peugeot.pujc_auto())
