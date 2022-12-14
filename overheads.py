
from gettext import find
from hashlib import new
from pathlib import Path
import re, csv
#opening file path
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

#opening empty variable
allvalues =[]
overheadvalue = 0

def overhead_function(x):
    #opening file path and reading it
    with fp.open(mode='r', encoding='UTF-8',newline="") as file:
        reading = csv.reader(file)
        next(reading)
   
        #bringing the expenses out
        for line in reading:
            allvalues.append(line[1])
        
    #turning values into float in order to use max() function
        newlist = [float(x) for x in allvalues]


    #using max() function to find the overhead expense and assigning it to overheadvalue variable
    overheadvalue = (max(newlist))

    overheadexpense = "Salary Expense"

    return_path = Path.cwd()/"Summary Report.txt"

    with return_path.open(mode = "a") as file:
        file.writelines(f"\n[HIGHEST OVERHEADS] SALARY EXPENSE: ${x*overheadvalue} ")



#using max() function to find the overhead expense and assigning it to overheadvalue variable
overheadvalue = (max(newlist))

overheadexpense = "Salary Expense"
