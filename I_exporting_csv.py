import csv
from pathlib import Path

data = [
    {
        "first_name": "Jericho",
        "last_name": "Smith",
        "pin": 123
    },
    {
        "first_name": "Samantha",
        "last_name": "Jones",
        "pin": 456
    }
]

header = ["first_name", "last_name", "pin"]

csvpath = Path("my_output.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write our header row first!
    csvwriter.writerow(header)

    # Then we can write the data rows
    for row in data:
        csvwriter.writerow(row.values())
        print(row.values())

#------------------------------
# Explanations 
# Si existe data anterior, la sobreescribe porque al ejecutar de nuevo no agrega tres filas mas

import csv
from pathlib import Path

data = [
    {
        "first_name": "Jericho",
        "last_name": "Smith",
        "pin": 123
    },
    {
        "first_name": "Samantha",
        "last_name": "Jones",
        "pin": 456
    }
]

header = ["first_name", "last_name", "pin"]     #En caso de que quiera headers como primera fila en mi csv

csvpath = Path("my_output.csv")
with open(csvpath, 'w', newline='') as csvfile: #comando newline='' es requerido por csv para que funcione bien el paquete
    csvwriter = csv.writer(csvfile)

    # Write our header row first!
    csvwriter.writerow(header)

    # Then we can write the data rows
    for row in data:
        csvwriter.writerow(row.values())

"""
    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects
    
"""