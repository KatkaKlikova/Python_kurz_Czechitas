sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Jaký je kód požadované součástky? ")
mnozstvi = int(input("Kolik kusů chcete? "))

if kod in sklad:
    dispozice = sklad[kod]
    if dispozice < mnozstvi:
        print(f"Lze prodat pouze omezené množství kusů: {dispozice}")
        pryc = sklad.pop(kod)
    elif dispozice == mnozstvi:
        print("Poptávku lze uspokojit v plné výši")
        pryc = sklad.pop(kod)
    else:
        print("Poptávku lze uspokojit v plné výši")
        sklad[kod] = dispozice - mnozstvi
else:
    print("Součástka není skladem.")

print(sklad)