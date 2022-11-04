#игра - 'Угадайка чисел'

import random

print('Привет! Это игра "Угадайка чисел"!')
print('Тебе нужно угадать число, сгененированное программой, в интервале [1, 100].')
print('Удачи!:)')

num_user = int(input())
num = random.randint(1, 100)

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
    