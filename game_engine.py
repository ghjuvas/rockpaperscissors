import random

content = {0: 'Камень', 1: 'Ножницы', 2: 'Бумага'}

dict_win = {
    'Камень': 'Ножницы',
    'Ножницы': 'Бумага',
    'Бумага': 'Камень'
}

def computer_play_choice(content):
    '''
    Выбор предмета компьютера с помощью библиотеки random
    '''

    comp_num = random.randint(0, 2)
    return content[comp_num]

def compare_choices(user_choice, comp_choice):
    '''
    Сравнение выборов пользователя и компьютера. Подведение итогов игры
    '''

    if user_choice == comp_choice:
        return 'Ничья!'
    elif comp_choice == dict_win[user_choice]:
        return 'Вы победили!'
    else:
        return 'Вы проиграли!'

def play(item):
    '''
    Собирательная функция для выполнения всех стадий игры
    '''

    computer_choice = computer_play_choice(content)
    result = compare_choices(item, computer_choice)

    return computer_choice, result