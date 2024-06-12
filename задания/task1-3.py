sp=[1,2,3,4,5,6,7,8,9,10]
num = int(input('введите целое число'))
flag = 0
for i in sp:
    if  i == num:
        flag = 1
   
if flag == 1:
    print('число есть в списке')
else:
    print('числа нет в списке')
          