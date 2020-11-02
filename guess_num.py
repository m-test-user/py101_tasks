"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""

if __name__ == '__main__':

    import random

    min_val = 0
    max_val = 1000000
    user_err = False
    user_try = '\nПривет, сыграем в игру? (и тогда я скажу как выйти)'
    count_try = 2
    rand_num = random.randint(min_val, max_val)
    kaom = '(-_-)'

    # print(rand_num)

    while True:
        
        print(user_try) 
        user_num = input(f'Угадай число от {min_val} до {max_val}: ')
        
        try:
            user_num = int(user_num)
        except ValueError:
            user_err = True

        if user_num == rand_num:
            print('Ты угадал! Как ты это сделал? Теперь ты можешь выйти!')
            input('Для выхода введи "exit" или нажми "enter": ')
            print('exit \n')
            break
        elif user_num == 'exit' or user_num == '':
            print('exit \n')
            break
        elif user_err == True:
            print('Что ты там ввел? Это не число! \n')
        elif user_num > max_val or user_num < min_val:
            print('Что ты там ввел? Это не входит в диапазон! \n')
        elif user_num > rand_num:
            print('Не угадал, у тебя число больше \n')
        elif user_num < rand_num:
            print('Не угадал, у тебя число меньше \n')
        
        user_try = f'Попытка {count_try} {kaom}'
        count_try += 1 
        user_err = False

        if count_try > 9:
            kaom = '(x_x)'