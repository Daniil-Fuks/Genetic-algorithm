import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from test_settings import SettingsWindow
from test_main import generate_animals


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QWidget):
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
        self.settings_window.show()
        # Создаем переменную self.settings_closed, которая обозначает, что окно настроек закрыто
        self.settings_closed = True

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

        f = open('settings.txt', mode='r', encoding='UTF-8').read().splitlines()
        print(f)
        # После принта self.settings_closed выдает ошибку
        print(self.settings_closed)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
