import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from test_settings import SettingsWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def generate_animals(num):  # Создание одной особи
    animal = ''
    list_parrants = []
    for i in range(num):
        for i in range(5):
            num = random.randint(0, 1)
            animal += str(num)
        list_parrants.append(animal)
        animal = ''
    return list_parrants


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test-disign.ui', self)
        self.initUI()

    def parents_set_text(self):
        num = int(self.select_herd_size.text())
        self.parants_lst = generate_animals(num)
        string = ''
        for i in self.parants_lst[:-1]:
            string += i + f' [{i.count("1")}], '
        string += self.parants_lst[-1] + f' [{i.count("1")}]'
        self.parent.setText(string)

    def settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.exec()
        f = open('settings.txt', mode='r', encoding='UTF-8').read().splitlines()
        f[0] = f[0].split(';')
        self.len = f[0][0]
        self.cnt = f[0][1]
        if f[0][2] == 'True':
            self.check_vis = '✅'
        else:
            self.check_vis = '❌'

        self.set_len.setText(str(self.len))
        self.set_cnt.setText(str(self.cnt))
        self.set_check_vis.setText(self.check_vis)

    def initUI(self):
        ...

        # Создание кнопки "создать стадо" и ее настройка

        # self.create_parants.clicked.connect(self.parents_set_text)

        # Вывод созданного стада
        # self.parent = QLabel(self)
        # self.parent.move(450, 0)
        # self.parent.setFont(QFont('Times New Roman', 10))
        # self.parent.resize(1000, 100)

        ##############################################################################
        self.text_setting_btn.clicked.connect(self.settings)
