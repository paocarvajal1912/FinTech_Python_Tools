"""Pathways to Success."""
print('\33c')
print("Let's start opening cvs files.....")
# @TODO: Import the Path tool from the pathlib library
from pathlib import Path


my_directory=Path(".")    # "." represents the current directory
print(my_directory)

# @TODO: Create a path to the `quarterly_data.csv` file
csvpath=Path("quarterly_data.csv")

# Print the relative path (the relative location of the file)
print(f"The relative CSV path is {csvpath}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is {csvpath.absolute()}")

#Import csv library
from pathlib import Path    #This line is already execute above, but kee it here for learning purposes
import csv 


with open(csvpath) as csvfile:
    data=csv.reader(csvfile)
    counter=0
    for row in data:
        print (counter,row)
        counter=counter+1


