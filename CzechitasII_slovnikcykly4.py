import math
recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

cena = 0
#Uložte si tuto strukturu do proměnné recept na začátek nového programu. 
#Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
for polozka in recept['ingredience']:
#delka = len(polozka[2]) ... musim odriznout posledni 3 znaky, tj. mezeru a kc, abych mohla prevest na desetinne cislo (float)
    cisla = polozka[2][0:(len(polozka[2])-3)]
    novy_cisla = float(cisla)
    cena += novy_cisla
print(cena)
zaokrouhleno = math.ceil(cena)
print(zaokrouhleno)
