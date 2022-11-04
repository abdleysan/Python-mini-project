#игра - 'Угадайка чисел'

import random

print('Привет! Это игра "Угадайка чисел"!')
print('Тебе нужно угадать число, сгененированное программой, в интервале [1, 100].')
print('Удачи!:)')

def is_valid(num_user1):
    if str(num_user1).isdigit() and 1 <= num_user1 <= 100:
        return True
    else:
        
        return 'А может быть все-таки введем целое число от 1 до 100?'

num_user = int(input())
num = random.randint(1, 100)

print(is_valid(num_user))

while num_user != num:
    if num_user > num:
        print('Слишком много, попробуйте еще раз')
        num_user = int(input())
        continue
    elif num_user < num:
        print('Слишком мало, попробуйте еще раз')
        num_user = int(input())
        continue
if num_user == num:
    print('Вы угадали, поздравляем!')