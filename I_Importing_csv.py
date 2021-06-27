print('\33c')
#Clean summary of the way to do things for visual purposes
import csv
from pathlib import Path

csvpath = Path("quarterly_data.csv")
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)


#------------------------------------------
#EXPLANATIONS

# Importing file
import csv
from pathlib import Path

csvpath = Path("quarterly_data.csv")
print(f"The path of the file: {csvpath} '\n\n'")

                               
with open(csvpath) as csvfile: #OBS: the terminal must be on the local path for this to run
                               #open() has a second optional parameter: r, w, r+ for reading (default), writting, and read+write 
                               #ex. open(csvpath,'r') 
    data = csv.reader(csvfile) #generated a csv reader object
    i=0
    matrix=[]
    for row in data:          #Forma eficiente de guardar la data en lista de linea por linea
        print(f"Imprimiendo linea a linea, que se transforma en las filas de una matriz: {row} ") 
        matrix.append(row)

print(f"This is the matrix grabbing the rows:{matrix}")
with open(csvpath) as csvfile: #after reading is close because of with, so need to be open again
    content_in_list=list(csvfile)#set the content of the file in one list. Not so great, becasue it keeps the full line as one string, including '\n'
print(f""" '\n\n' You can set all the content of the file in a list using list(cvsfile):
    {content_in_list}""")  #  
    
print('\n \n')
print(f"display content of data with cvs.reader(): {data}")  #This displays <_csv.reader object at 0x7fb61a1e0890>
print(f"data con cvsfile.read(): {data}") #forma equivalente de hacer lo mismo

