from cgi import test
from xml.dom import UserDataHandler
import requests
from pathlib import Path 

api_key = "F2UE00AWKLCI7DKV"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo ={api_key}"

response = requests.get(url)

data = response.json()

#print(data)

values = data.values()
#to extract the values from the dictionary
list_ = list(values)
#convert the dict.values into a list
remove = list_.pop()
#to remove the key value
list_2 = list(remove.values())
#to extract the value s from the dict and conver it to list

rate = float(list_2[4])
#to extract the exchange rate from USD to SGD
currency_rate = 0


def api_function():
    return rate

file_path = Path.cwd()/"Summary Report.txt"

with file_path.open(mode = "a") as file:
        file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD={rate}")






