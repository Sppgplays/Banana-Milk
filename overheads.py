from gettext import find
from hashlib import new
from pathlib import Path
import re, csv
#opening file path
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

#opening empty variable
allvalues =[]

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