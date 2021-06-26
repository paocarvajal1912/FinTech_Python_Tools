print('\033c')
#Como trabajar con listas - Asignacion
clean15_NoNeedToBeOrganic=["avocados", "pineapple", "cabbage", "onions",\
    "asparagus","mangos","melon tuna","melon calameño"]
#print(clean15_NoNeedToBeOrganic, end='\n')
print(clean15_NoNeedToBeOrganic[0:len(clean15_NoNeedToBeOrganic)])
# notar que el ultimo indice no es incluido. El primero si. Primer indice es cero.
largo_de_la_lista=len(clean15_NoNeedToBeOrganic)
print (f"El largo de la lista es: {largo_de_la_lista}")

Numero_Lista=1
print(f"El numero {Numero_Lista} de la lista es: {clean15_NoNeedToBeOrganic[Numero_Lista-1]}")

#Ahora le vamos a incluir algunos nuevos elementos
#Se usa la función "append"
clean15_NoNeedToBeOrganic.append("coliflower")
print(f"La nueva lista es: {clean15_NoNeedToBeOrganic}")






