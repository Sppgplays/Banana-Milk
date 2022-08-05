from pathlib import Path 
import re, csv
from tkinter import N
from tkinter.messagebox import YES
from unittest import skip

file_path = Path.cwd()/"csv_reports"/"Profit & Loss.csv"
pl_list = []
difference_list = []
flat_difference_list =[]
day_list = []
return_list = []


def profitloss_function(x):
  "This Function takes in 1 variable (x)"
  "This function will find if there are any loss or profit for all days"
  count = -1
  surplus = 0
  with file_path.open(mode='r', encoding='UTF-8', newline="") as file: 
    reading = csv.reader(file)
    next (reading)

    #fetch the values in seperate lists

    for line in reading:
      pl_list.append(line[1])
      day_list.append(line[0])

  #convert values to int
  for strings in range(0, len(pl_list)):
    pl_list[strings] = int(pl_list[strings])

    #find the differences in the different days
  for differences in range (len(pl_list)-1):
    difference_list.append(pl_list[differences+1]-pl_list[differences])

    #return answers
  for number in difference_list:
      count = count + 1
      if number < 0:
        return_list.append(f"\n[PROFIT DEFICIT] DAY:{day_list[count]}, AMOUNT: {x*difference_list[count]} ")
        

      elif number > 0:
        surplus = surplus + 1
        

        if surplus == 5:
                return_list.append(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

  return_path = Path.cwd()/"Summary Report.txt"

  with return_path.open(mode = "a") as file:
      file.writelines(return_list)



  