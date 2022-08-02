from cgi import test
from xml.dom import UserDataHandler
import requests

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

def convert(x):
    converting =  (x * rate)
    #to use the exchange rate to find the value in SGD
    index = "{:.2f}".format(converting)
    #to round the value to 2 decimal place
    return f"{converting} SGD"

print(convert(12))




