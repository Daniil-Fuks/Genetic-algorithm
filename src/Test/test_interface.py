import random
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from test_classes import Herd
from test_settings import SettingsWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# Функция, которая генерирует одного ребенка
def new_child(winners, num):
    child_1 = winners[random.randint(0, num)]
    child_2 = winners[random.randint(0, num)]

    while child_1 == child_2:
        child_2 = winners[random.randint(0, num)]

    split = random.randint(0, num - 1)
    child = child_1[0][:split] + child_2[0][split:]
    return child


# Функция, производящая мутациюa
def mutation(lst, prob):
    herd = []
    buffer = []
    for i in range(len(lst)):
        ind = ''
        for z in range(len(lst[i][0])):
            flag = random.randint(1, 100)
            obj = lst[i][0][z]
            if flag <= prob:
                if obj == '1':
                    ind += '0'
                elif obj == '0':
                    ind += '1'
            else:
                ind += obj
        herd.append(ind)
    for i in range(len(herd)):
        buffer.append([herd[i], f'[{herd[i].count("1")}]'])
    return buffer


def show_herd(item, herd, num):
    con = sqlite3.connect('test-db.sqlite3')
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM herd WHERE number_herd = {num}').fetchall()
    for i in range(len(res)):
        item.addItem(f'{res[i][1]} [{res[i][2]}]')
    item.addItem(f'Среднее значение: {str(round(float(herd.get_middle_value(num)), 4))}')


def clean_db():
    con = sqlite3.connect('test-db.sqlite3')
    cur = con.cursor()
    cur.execute(f'DELETE FROM herd; ').fetchall()
    cur.execute(f'DELETE FROM sqlite_sequence WHERE name="herd"').fetchall()
    con.commit()


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test-main-disign.ui', self)
        self.initUI()
        self.herd = Herd()
        self.loops = 0
        self.mutation = 0
        self.check_vis = False
        self.middle_value = []
        self.parants_list.hide()
        self.new_animals_lst.hide()
        self.label_2.hide()
        self.label_3.hide()

    # С помощью этой функции создается целое стадо

    def start(self):
        self.parants_list.show()
        self.new_animals_lst.show()
        self.label_2.show()
        self.label_3.show()
        self.start_btn.hide()

        # Очистка БД после прошлых использований
        clean_db()

        # Генерация первого стада
        self.herd.generate_animals()
        show_herd(self.parants_list, self.herd, 1)

        for i in range(int(self.loops)):
            if i > 0:
                self.herd.set_first_iteration_flag()

            self.middle_value.append(self.herd.get_middle_value(1))

            # Произведение битвы, средняя сила стада записывается в список
            self.herd.last_id = self.herd.get_last_id()
            self.herd.fight()
            self.middle_value.append(self.herd.get_middle_value(2))

            # Рождение нового поколения
            self.herd.reproduction()
            self.middle_value.append(self.herd.get_middle_value(3))

            # Произведение мутации, запись среднего значения в список
            self.herd.mutation(10)
            self.herd.cleaning()
            if i + 1 == int(self.loops):
                show_herd(self.new_animals_lst, self.herd, 1)
                break


        #
        #     # Происходит мутация и новое стадо становится родительским. На этом моменте можно сделать цикл.
        #     self.parants = mutation(self.children, self.mutation_chanse)
        #
        # # Вывод последней вариации стада
        # for i in range(len(self.parants)):
        #     self.new_animals_lst.addItem(f'{self.parants[i][0]} {self.parants[i][1]}')
        # middle = get_middle(self.parants)
        # self.middle_stat.append(middle)
        # self.new_animals_lst.addItem(f'Среднее значение: {middle}')

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
        self.mutation_chanse = int(f[0][4]) / 100
        self.mutation_chanse_output = f[0][4]

        if f[0][2] == 'True':
            self.check_vis = '✅'
        else:
            self.check_vis = '❌'

        self.set_len.setText(str(self.len))
        self.herd.set_len_ind(self.len)
        self.set_cnt.setText(str(self.cnt))
        self.herd.set_quantity(self.cnt)
        self.set_check_vis.setText(self.check_vis)
        self.set_loop_cnt.setText(self.loops)
        self.set_mutation.setText(self.mutation_chanse_output + '%')

    def initUI(self):
        self.start_btn.clicked.connect(self.start)

        ##############################################################################
        self.text_setting_btn.clicked.connect(self.settings)


def execpt_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = execpt_hook
    app = QApplication(sys.argv)
    ex = Interface()
    ex.show()
    sys.exit(app.exec())
