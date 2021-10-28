import tkinter as tk
from game_engine import content
from game_engine import play

context = {
    'comp_choice_label': None,
    'result_label': None,
    'stats_label': None,
    'wins': 0,
    'ties': 0,
    'fails': 0
}

main_window = tk.Tk()
main_window.title('Камень, Ножницы, Бумага')


class someLabel:

    def __init__(self, text, row):
        self.text = text
        self.row = row
        self.label = tk.Label(main_window, text=self.text, font='14')
        self.label.grid(column=1, row=self.row)

    def remove(self):
        self.label.grid_remove()

item = tk.IntVar()


class someButton:

    def __init__(self, text, column, row, value, item):
        self.text = text
        self.column = column
        self.row = row
        self.value = value
        item = item

    def radiobutton(self):
        rb = tk.Radiobutton(main_window,
        text=self.text,
        font='14',
        variable=item,
        value=self.value)
        rb.grid(column=self.column, row=self.row, sticky='s')

    def button(self):
        btn = tk.Button(main_window,
        text='Играть!',
        font='14',
        command=lambda: play_cmnd(item))
        btn.grid(column=self.column, row=self.row, sticky='s')


main_text = '''Добро пожаловать в игру!
Выберите свой предмет, нажав на соответствующую кнопку.
Нажмите "Играть", чтобы проверить свой выбор.
'''
someLabel(main_text, 0) # приветственная надпись

wins = context['wins']
ties = context['ties']
fails = context['fails']

stats_text = f'Победы: {wins} Ничьи: {ties} Проигрыши: {fails}'
someLabel(stats_text, 1) # начальная статистика

btn_rock = someButton('Камень', 0, 2, 0, item)
btn_rock.radiobutton()
btn_scissors = someButton('Ножницы', 1, 2, 1, item)
btn_scissors.radiobutton()
btn_paper = someButton('Бумага', 2, 2, 2, item)
btn_paper.radiobutton()

btn_play = someButton('Играть', 1, 3, None, item)
btn_play.button()

def stats(result):
    '''
    Смена значений статистики
    '''

    num_ties = context[result]
    num = num_ties + 1
    context[result] = num

    wins = context['wins']
    ties = context['ties']
    fails = context['fails']

    if context['stats_label']:
        context['stats_label'].remove()
    stats_text = f'Победы: {wins} Ничьи: {ties} Проигрыши: {fails}'
    stats_label = someLabel(stats_text, 1)
    context['stats_label'] = stats_label


def play_cmnd(num_item):
    '''
    Сбор данных о выбранном предмете.
    Передача данных для обработки.
    Выдача результата.
    Инициализация смены значений статистики
    '''

    chosen_item = num_item.get()

    for var, name in content.items():
        if var == chosen_item:
            full_result = play(name)
            result = full_result[1]

    comp_choice = full_result[0]

    if context['comp_choice_label']:
        context['comp_choice_label'].remove()
    if context['result_label']:
        context['result_label'].remove()

    comp_choice_label = someLabel(comp_choice, 4)
    res_label = someLabel(result, 5)

    context['comp_choice_label'] = comp_choice_label
    context['result_label'] = res_label

    if result == 'Ничья!':
        stats('ties')
    if result == 'Вы победили!':
        stats('wins')
    if result == 'Вы проиграли!':
        stats('fails')

    return result


main_window.mainloop()
