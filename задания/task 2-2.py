def delivery_sum(amount):
    if amount == 0:
        print('Стоимость доставки 0 $')
        return 0
    else:
        summa = 10.95 + (amount - 1) * 2.95
        print(f'Стоимость доставки составит {summa} $')
        return summa

positions = int(input('Введите количество позиций в заказе'))
delivery_sum(positions)
        