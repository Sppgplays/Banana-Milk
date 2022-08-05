from pathlib import Path 
import re, csv
from tkinter import N
from tkinter.messagebox import YES
from unittest import skip

file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
coh_list = []
difference_list = []
flat_difference_list =[]
day_list = []
returncoh = []


def coh_function(forex):
  "This Function takes in 1 variable (x)"
  "This function will find if there are any cash deficit or if there is cash surplus for all days"
  count = -1
  surplus = 0
  #open cash on hand file
  with file_path.open(mode='r', encoding='UTF-8', newline="") as file: 
    reading = csv.reader(file)
    #Skip Heading
    next (reading)
    #fetch values into seperate list
    for line in reading:
      coh_list.append(line[1])
      day_list.append(line[0])

    #convert strings into integer in list
  for strings in range(0, len(coh_list)):
    coh_list[strings] = int(coh_list[strings])
    #find the difference in the days
  for differences in range (len(coh_list)-1):
    difference_list.append(coh_list[differences+1]-coh_list[differences])

 #return if there is any cash deficit or if there is a cash surplus
  for number in difference_list:
      count = count + 1
      if number < 0:
        returncoh.append(f"\n[CASH DEFICIT] DAY:{day_list[count]}, AMOUNT: {difference_list[count]} ")
        surplus = surplus + 1

      elif (number > 0 and surplus == 0):
        returncoh.append(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

  return_path = Path.cwd()/"Summary Report.txt"

  with return_path.open(mode = "a") as file:
      file.writelines(returncoh)


  

