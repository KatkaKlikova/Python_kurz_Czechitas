jmeno = "Johanka"
print(f"{jmeno}@czechitas.cz")

jmeno_a_prijmeni = input("Zadej své jméno a příjmení: ")

print(f"Malými písmeny: {jmeno_a_prijmeni.lower()}")
print(f"Velkými písmeny: {jmeno_a_prijmeni.upper()}")

#rozdelim na kr. jmeno a prijmeni, aby se dalo pracovat s kazdym zvlast
udaje = jmeno_a_prijmeni.split(" ")
jmeno = udaje[0].capitalize()
prijmeni = udaje[1].capitalize()
print(f"Kapitálky: {jmeno} {prijmeni}")
print(f"Iniciály: {jmeno[0]}. {prijmeni[0]}.")

if len(jmeno) > 5:
    print(f"Zkrácené jméno: {jmeno[0]}. {prijmeni}")
else:
    print(f"Jméno: {jmeno} {prijmeni}")
