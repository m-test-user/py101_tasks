"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    
    pass_value = [] + list(input('Input your pass: '))

    if len(pass_value) < 8:
        print('Bad pass')
        exit()
    
    count_alpha = [element for element in pass_value if element.isalpha()]
    count_digit = [element for element in pass_value if element.isdigit()]

    if len(count_alpha) > 0 and len(count_digit) > 0:
        print('Good pass')
    else:
        print('Bad pass')