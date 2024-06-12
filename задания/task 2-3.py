import random
def password():
    sp = []
    for i in range (10):
        number = random.randint(1,9)
        sp.append(number)
        
    return sp    

gen_password = password()
print('Сгенерированный пароль:')
print(''.join(map(str,gen_password)))