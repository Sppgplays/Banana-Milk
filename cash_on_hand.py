from pathlib import Path 
import re, csv
from tkinter import N

file_path = Path.cwd()/"CSV_reports"/"Cash On Hand.csv"
empty_list = []

with file_path.open(mode='r', encoding='UTF-8', newline="") as file: 
  reading = csv.reader(file)
  next (reading)

  for line in reading:
    empty_list.append(line[1])
print(empty_list)

