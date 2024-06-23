import requests
import json

response = requests.get("https://fakestoreapi.com/products/categories")
categories = response.json()

print('доступные категории:')
for category in categories:
    print(category)

selected_category = input('Выберите категорию')
response = requests.get(f"https://fakestoreapi.com/products/category/{selected_category}")

products = response.json()

for product in products:
  print(f"Название: {product['title']}")
  print(f"Цена: {product['price']}")
  print(f"Описание: {product['description']}")
  print("-------------------------")
        