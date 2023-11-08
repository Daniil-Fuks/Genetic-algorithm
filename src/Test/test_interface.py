import random
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from test_settings import SettingsWindow
from test_classes import Herd


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def get_middle(lst):
    middle = []
    for i in lst:
        middle.append(int(i[1][1:-1]))
    return round(sum(middle) / len(middle), 4)


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
        ind = ''
    for i in range(len(herd)):
        buffer.append([herd[i], f'[{herd[i].count("1")}]'])
    return buffer

def show_herd(item, herd):
    con = sqlite3.connect('test-db.sqlite3')
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM herd').fetchall()
    for i in range(len(res)):
        item.addItem(f'{res[i][1]} [{res[i][2]}]')
    item.addItem(f'Среднее значение: {str(herd.get_middle_value())}')

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


    def start(self, loops):
        self.parants_list.show()
        self.new_animals_lst.show()
        self.label_2.show()
        self.label_3.show()
        self.start_btn.hide()

        clean_db()
        self.herd.generate_animals()
        show_herd(self.parants_list, self.herd)
        self.middle_value.append(self.herd.get_middle_value())

        self.herd.fight()

        """
        2. Битва
        3. Размножение
        4. Мутация
        """

        #     # Получаем новое стадо после произвеения битвы
        #     for _ in range(len(self.parants)):
        #         self.winners.append(fight(self.parants, len(self.parants) - 2))
        #     middle = get_middle(self.winners)
        #     self.middle_stat.append(middle)
        #
        #     # Создаем потомство
        #     for i in range(len(self.winners)):
        #         child = new_child(self.winners, len(self.winners) - 1)
        #         buffer = [child, f'[{child.count("1")}]']
        #         self.children.append(buffer)
        #     middle = get_middle(self.children)
        #     self.middle_stat.append(middle)
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
        self.set_cnt.setText(str(self.cnt))
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
