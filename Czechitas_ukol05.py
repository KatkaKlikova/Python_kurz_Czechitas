'''Mějme zadaný následující seznam naměřených teplot. 
Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech 
- ráno, v poledne, večer a v noci.'''
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vytvoř seznam průměrných teplot pro každý den.
prumer = [round(sum(den)/len(den), 2) for den in teploty]
print(prumer)
#Vytvoř seznam ranních teplot.
rano = [den[0] for den in teploty]
print(rano)

#Vytvoř seznam nočních teplot.
noc = [den[3] for den in teploty]
print(noc)

#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledne_noc = [[den[1], den[3]] for den in teploty]
print(poledne_noc)

teploty_bonus = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
'''Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, 
kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
{den: průměrná teplota}'''

prumerne_teploty = {den[0]:round((sum(den[1:])/(len(den)-1)),2) for den in teploty_bonus}
print(prumerne_teploty)
