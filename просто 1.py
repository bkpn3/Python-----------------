import random
def generate_random_sp(a,b):
    sp = []
    for i in range(10):
        number = random.uniform(a, b)
        sp.append(number)
    return sp
print('Добрый день! Сейчас вам нужно будет ввести три диапазона')
for i in range(3):
    num1 = float(input(f'Введите начало {i + 1} диапазона'))
    num2 = float(input(f'Введите конец {i + 1} диапазона'))
    random_numbers = generate_random_sp(num1, num2)
    print(random_numbers)
print('Программа завершена')