import random
import sys

from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QDialog

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
        self.set_len = f[0][0]
        self.set_cnt = f[0][1]
        if f[0][2] == 'True':
            self.set_check_vis = True
        else:
            self.set_check_vis = False

        print(self.set_len, self.set_cnt, self.set_check_vis)





        # dlg = QDialog(self)
        # dlg.setWindowTitle("HELLO!")
        # dlg.exec()


    def initUI(self):
        self.setGeometry(100, 100, 1100, 700)
        self.setWindowTitle('Эммитация генетического алгоритма')

        # Создание кнопки "создать стадо" и ее настройка

        # self.create_parants = QPushButton("Создать стадо", self)
        # self.create_parants.move(40, 50)
        # self.create_parants.resize(200, 30)
        # self.create_parants.clicked.connect(self.parents_set_text)

        # ---------------------------------------------------------------
        # Создание текста и поля ввода для указания кол-ва особей в стаде
        # ---------------------------------------------------------------

        # self.select_herd_size = QLineEdit(self)
        # self.select_herd_size.resize(50, 25)
        # self.select_herd_size.move(230, 35)
        #
        # self.select_herd_size_text = QLabel(self)
        # self.select_herd_size_text.setText('Количество особей в стаде:')
        # self.select_herd_size_text.setFont(QFont('Times New Roman', 11))
        # self.select_herd_size_text.move(10, 35)

        # Вывод созданного стада

        # self.text1 = QLabel(self)
        # self.text1.move(450, 0)
        # self.text1.setText("Родительское стадо:")
        # self.text1.setFont(QFont('Times New Roman', 15))
        #
        # self.parent = QLabel(self)
        # self.parent.move(450, 0)
        # self.parent.setFont(QFont('Times New Roman', 10))
        # self.parent.resize(1000, 100)

        ##############################################################################

        self.text_setting_btn = QPushButton('Настройки', self)
        self.text_setting_btn.move(50, 25)
        self.text_setting_btn.clicked.connect(self.settings)

        self.label = QLabel(self)
        self.label.setText('Длина одной особи:')
        self.label.resize(150, 30)
        self.label.move(20, 100)
        self.label.show()
