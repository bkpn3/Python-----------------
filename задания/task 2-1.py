a = 10
b = 20

def area(number):
    if number > a and number < b:
        print('Число входит в диапазон')
        return True
    else:
        print('Число не входит в диапазон')
        return False
nom = int(input('Введите число'))
area(nom)
