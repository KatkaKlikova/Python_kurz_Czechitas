'''Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. 
Bodová rozhraní (vztahují se na součet) najdeš zde:
1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně
 Výsledný slovník ulož jako JSON do souboru znamky.json.'''

import json

with open ('body.json', mode='r', encoding='utf-8') as file:
    body = json.load(file)

with open ('bonusy.json', mode='r', encoding='utf-8') as file:
    bonusy = json.load(file)

celkem = {}

for jmeno, hodnota in body.items():
    if jmeno in bonusy:
        celkem[jmeno] = hodnota + bonusy[jmeno]
    else:
        celkem[jmeno] = hodnota

znamky = {}

for jmeno, hodnota in celkem.items():
    if hodnota >= 90:
        znamky[jmeno] = 1
    elif hodnota >= 70 and hodnota < 90:
        znamky[jmeno] = 2
    elif hodnota >= 50 and hodnota < 70:
        znamky[jmeno] = 3
    elif hodnota >= 30 and hodnota < 50:
        znamky[jmeno] = 4   
    else:
        znamky[jmeno] = 5

with open ('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(znamky, file, ensure_ascii=False)