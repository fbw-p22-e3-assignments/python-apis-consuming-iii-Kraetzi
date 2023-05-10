import requests

import pprint

headers = {
    "content-type": "application/json"
}
task_input = int(input("give the number of the task you want to show"))

if task_input == 1:    
    url = "https://fakerapi.it/api/v1/companies?_quantity=5"
elif task_input == 2:
    url = "https://fakerapi.it/api/v1/persons?_quantity=50&_birthday_start=1995-01-01&_locale=en_EN"
elif task_input == 3:
    url = "https://fakerapi.it/api/v1/persons?_quantity=50&_birthday_start=1995-01-01&_locale=en_EN"
elif task_input == 4:
    url = "https://fakerapi.it/api/v1/credit_cards?_quantity=60&_locale=es_ES"
elif task_input == 5:
    url = "https://fakerapi.it/api/v1/products?_quantity=47&_price_min=50"
elif task_input == 6:
    url = "https://fakerapi.it/api/v1/custom?_quantity=10&customfield1=pokemon&customfield2=website&customfield3=name"    

response =requests.get(url, headers=headers)

pprint.pprint(response.json())