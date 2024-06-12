import requests
import json
import pprint

url = 'https://fakestoreapi.com/users'

fio = input('о каком пользователе Вы хотите получить информацию?')
response = requests.get(url).json()
flag = False
for item in response:
    if item['name']['lastname'] == fio:
        print(f'Имя: {item["name"]["firstname"]} Фамилия:{item["name"]["lastname"]}')
        print(f' Телефон: {item["phone"]}\n Email: {item["email"]}')
        flag = True
if flag == False:

    print('Нет такого пользователя')
        