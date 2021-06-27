print('\033c')
#Format as a a list of lists
table_data_list_of_lists = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]

print(table_data_list_of_lists, end='\n \n')

#Foramt as a dictionary
table_data_list_of_dics = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {
        "Ticker": "GOOG",
        "Open": 1409.1,
        "Close": 1408.2
    }
]

print(table_data_list_of_dics, end='\n\n')

#retrieving Amazon:
print("Amazon:",table_data_list_of_lists[2])
print("Amazon:", table_data_list_of_dics[1])
#OBS: Me gusta mas la lista de listas

#Retrieving opening prices of amazon
print("Amazon:")
print("Opening price:",table_data_list_of_lists[2][1], end='\n \n')

#Retrieving opening prices of all in list of list
print("Retrieving tickers")
for row in table_data_list_of_lists:
    ticker=row[0]
    print(ticker)

print("Imprimiento closing prices of all tickers desde lista multiple")
#print(table_data_list_of_lists[0])
for row in table_data_list_of_lists:
    [ticker, open_price]=row[0:2]
    print(ticker, open_price)

print('\n\n')


#Imprimiento closing prices using list of diccionaries
print (table_data_list_of_dics, end='\n\n')
print("Imprimiento closing prices of all tickers desde lista de diccionarios")
for ticker_price_set in table_data_list_of_dics:
    ticker=ticker_price_set['Ticker']
    open_price=ticker_price_set['Open']
    ticker2=ticker_price_set.get('Ticker') #Usar comando get permite dar valor por defecto
    print(ticker, ticker2,open_price) 

#Uso de get: dict.get(key[, default])
#dictionary = {"message": "Hello, World!"}
#data = dictionary.get("message", "")




print("Imprimiento closing prices of all tickers desde lista de diccionarios trabajado en forma resumida")
for ticker_price_set in table_data_list_of_dics:
    [ticker,open_price]=[ticker_price_set['Ticker'],ticker_price_set['Open']]
    print(ticker,open_price) 

print('\n\n')

#Uso de comando get











