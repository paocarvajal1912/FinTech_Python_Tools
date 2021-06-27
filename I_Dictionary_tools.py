
loan_solito ={
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000}

item_del_loan=loan_solito.items()
print(f"\n El tipo cuando uso items es: {type(item_del_loan)}")

print(f"Imprimo loan_solito.items() del tipo anterior. Parece una lista de items, pero no lo es \
sino mas bien es una lista-iterable: \n {item_del_loan} \n\n")

## VALUES AND KEYS iterables tambien
loan_solito_values=loan_solito.values()
loan_solito_keys=loan_solito.keys()

print(f"Loans values using method loan_solito.values(): \n {loan_solito_values}")
print(f"Loans keys using method loan_solito.keys(): \n {loan_solito_keys}")
print("Lo bueno de estos elementos es que son iterables.")
print(f"Ahora voy a imprimir desde una lista de diccionarios \n")

"""
Listas iterables son utiles para imprimir csv files linea por linea (me imagino, por confirmar)
"""

#lista de diccionarios
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans=[]

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    price_of_unclassified_loan=loan["loan_price"]
    if price_of_unclassified_loan<=500:
        inexpensive_loans.append(loan)


# @TODO: Print the `inexpensive_loans` list
#Paola: will apply an iteration so the format is readable
print("INEXPENSIVE LOANS:")

for loan in range(0,len(inexpensive_loans)):
    for key, value in inexpensive_loans[loan].items():
        print(f"[{loan}] {key} : {value}")       #takes values in the FOR line
    print('\n')
    print(f"Iterating on the dictionary iterates on keys \n")
    for key in inexpensive_loans[loan]:        #iteration on dictionary would only iterate on keys as string
        print(f"the key is: {key}          and the type is: {type(key)}")                       
    print(f"Iterating key and value using .items() \n")
    for key, value in inexpensive_loans[loan].items(): #iteration on items allows to capture both as string
        print(f"the key is: {key}          and the type is: {type(key)}")   
        print(f"the value is: {value}          and the type is: {type(value)}")                    
        


