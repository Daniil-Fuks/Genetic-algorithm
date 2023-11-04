import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from test_settings import SettingsWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def generate_animals(cnt, len_ind):  # Создание первого стада
    animal = ''
    list_parrants = []
    force_num = []
    for i in range(cnt):
        for i in range(len_ind):
            num = random.randint(0, 1)
            animal += str(num)
        animal = f'{animal}    [{animal.count("1")}]'
        force_num.append(animal.count("1"))
        list_parrants.append(animal)
        animal = ''
    middle = sum(force_num) / len(force_num)
    list_parrants.append(f'Среднее значение: {round(middle, 4)}')
    return list_parrants


def get_middle(lst):
    middle = []
    for i in lst:
        middle.append(int(i[1][1]))
    return sum(middle) / len(middle)


def fight(animals, cnt):  # Создание битвы
    num = random.randint(0, cnt)
    num2 = random.randint(0, cnt)
    if num == num2:
        return animals[num]
    else:
        if int(animals[num][1][1]) > int(animals[num2][1][1]):
            return animals[num]
        else:
            return animals[num2]


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test-main-disign.ui', self)
        self.initUI()
        self.cnt = 0
        self.len = 0
        self.loops = 0
        self.check_vis = False
        self.middle_stat = []
        self.winners = []
        self.parants_list.hide()
        self.new_animals_lst.hide()
        self.label_2.hide()
        self.label_3.hide()

    # С помощью этой функции создается целое стадо
    def create_parents(self):
        self.parants_lst = generate_animals(int(self.cnt), int(self.len))
        return self.parants_lst

    def start(self, loops):
        """
        1. После нажатия кнопки должно создаваться только одно родительское стадо.
        2. Далее это выбирается 6 пар из этого стада, производится битва (после битвы остаются 6 сильнейших особей)
        3. Особи размножаются, ДНК делится в рандомном месте, так появляется новое стадо.
        4. Новое стадо мутирует и встает на место родительского стада.
        """
        self.parants = self.create_parents()

        self.parants_list.show()
        self.new_animals_lst.show()
        self.label_2.show()
        self.label_3.show()
        self.start_btn.hide()

        # Отображение первого стада
        for i in self.parants:
            self.parants_list.addItem(i)

        # Добавляем среднее значение в общую статистику
        middle = float(self.parants[-1].split()[2])
        self.middle_stat.append(middle)

        # Обработка списка для удобного использования функции fight().
        for i in range(len(self.parants)):
            self.parants[i] = self.parants[i].split()

        # Получаем и отображаем новое стадо после произвеения битвы
        for _ in range(len(self.parants) - 1):
            self.winners.append(fight(self.parants, len(self.parants) - 2))
        for i in range(len(self.winners)):
            winner = self.winners[i]
            self.new_animals_lst.addItem(f'{winner[0]} {winner[1]}')
        self.new_animals_lst.addItem(f'Среднее значение: {round(get_middle(self.winners), 4)}')

    #     for i in range(int(self.loops) - 1):
    #         self.start_btn.hide()
    #         self.listWidget.show()
    #     if self.check_vis == '✅':
    #         plt.plot(self.middle_stat)
    #         plt.show()
    #     else:
    #         lst1 = self.create_parents()
    #         for i in range(len(lst1) - 1):
    #             self.listWidget.addItem(lst1[i])
    #         self.listWidget.addItem(f'Средняя сила: {lst1[-1]}')
    #         self.middle_stat.append(lst1[-1])

    def settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.exec()
        f = open('settings.txt', mode='r', encoding='UTF-8').read().splitlines()
        f[0] = f[0].split(';')
        self.len = f[0][0]
        self.cnt = f[0][1]
        self.loops = f[0][3]
        if f[0][2] == 'True':
            self.check_vis = '✅'
        else:
            self.check_vis = '❌'

        self.set_len.setText(str(self.len))
        self.set_cnt.setText(str(self.cnt))
        self.set_check_vis.setText(self.check_vis)
        self.set_loop_cnt.setText(self.loops)

    def initUI(self):
        self.start_btn.clicked.connect(self.start)

        ##############################################################################
        self.text_setting_btn.clicked.connect(self.settings)
