'''Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", 
pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.jso'''

import json

with open('body.json', encoding='utf-8') as file:
    bodiky = json.load(file)

prospech = {}

for item, values in bodiky.items():
    prospech[item] = values

for item, values in prospech.items():
    if values >= 60:
        prospech[item] = "Pass"
    else:
        prospech[item] = "Fail"

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(prospech, file, ensure_ascii=False)
