print('\33c')
# Uso de palabras, mayusculas, etc
word="WoRd"
print(word.upper())
print(word.lower())
print(word.title())

palabras=["esToy","JUganDO","A","CoRriGiendO mIs PalaBrAs Mal esCritas"]

for una_palabra in palabras:
    print(f"original:      {una_palabra}")
    print(f"uso de .upper: {una_palabra.upper()}")
    print(f"uso de .lower: {una_palabra.lower()}")
    print(f"uso de .title: {una_palabra.title()}")

print("\n Ahora me sali del iterador, y terminamos \n")