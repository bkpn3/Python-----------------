def check_password(password):
    if len(password) > 8:
        print('Пароль надёжный')
        return True
    else:
        print('Пароль ненадёжный')
        return False

password = input('Введите пароль:')


while check_password(password) == False:
    print('Введите новый пароль')
    password = input('введите пароль')
    check_password(password)