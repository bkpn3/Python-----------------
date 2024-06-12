sp = [1,2,3,4,5,6,7,8,9,10]
chet = 0
nechet = 0
for num in sp:
    if num % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f'Количество четных чисел равно {chet}, Количество нечетных чисел равно {nechet}')