import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from test_settings import SettingsWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def generate_animals(cnt, len):  # Создание одной особи
    animal = ''
    list_parrants = []
    numbers = []
    for i in range(cnt):
        for i in range(len):
            num = random.randint(0, 1)
            animal += str(num)
        animal = f'{animal}    [{animal.count("1")}]'
        #numbers.append(animal.count("1"))
        list_parrants.append(animal)
        animal = ''
    #print(len(numbers))
    return list_parrants


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test-main-disign.ui', self)
        self.initUI()
        self.cnt = 0
        self.len = 0
        self.loops = 0
        self.check_vis = False
        self.listWidget.hide()

    # С помощью этой функции создается целое стадо
    def create_parents(self):
        self.parants_lst = generate_animals(int(self.cnt), int(self.len))
        return self.parants_lst

    def start(self):
        self.start_btn.hide()
        self.listWidget.show()
        lst1 = self.create_parents()
        for i in range(len(lst1) - 1):
            self.listWidget.addItem(lst1[i])
        #self.listWidget.addItem(f'Средняя сила: {lst1[-1]}')

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
