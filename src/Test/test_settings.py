import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton, QCheckBox


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 260, 150)
        self.setWindowTitle('Настройки')

        # Настройка количества особей в стаде
        self.text_setting_cnt = QLabel(self)
        self.text_setting_cnt.setText('Количество особей в стаде:')
        self.text_setting_cnt.move(10, 45)
        self.text_setting_cnt.setFont(QFont('Verdana', 10))

        self.input_cnt = QLineEdit(self)
        self.input_cnt.move(210, 45)
        self.input_cnt.resize(30, 20)

        # Настройка длины одного животного
        self.text_len_animal = QLabel(self)
        self.text_len_animal.setText('Длина одного животного:')
        self.text_len_animal.move(10, 10)
        self.text_len_animal.setFont(QFont('Verdana', 10))

        self.input_len = QLineEdit(self)
        self.input_len.resize(30, 20)
        self.input_len.move(195, 10)

        # Настройка визуализации
        self.checkbox_vision_text = QLabel(self)
        self.checkbox_vision_text.setText('Отображение визуализации:')
        self.checkbox_vision_text.setFont(QFont('Verdana', 10))
        self.checkbox_vision_text.move(10, 80)

        self.checkbox_vision = QCheckBox(self)
        self.checkbox_vision.move(210, 82)

        # Кнопка сохранения
        self.button_save = QPushButton('Сохранить', self)
        self.button_save.move(90, 110)
        self.button_save.clicked.connect(self.save_settings)

        # Уведомление о сохранении

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        line1 = QPainter()
        # Начинаем процесс рисования
        line1.begin(self)
        self.draw(line1)
        # Завершаем рисование
        line1.end()

    def draw(self, line):
        # Задаем кисть
        line.setBrush(QColor(255, 0, 0))
        # Рисуем прямоугольник заданной кистью
        line.drawLine(20, 35, 180, 35)
        line.drawLine(20, 70, 180, 70)

    def save_settings(self):
        if self.checkbox_vision.checkState() == 2:
            self.checkbox_vision_res = True
        elif self.checkbox_vision.checkState() == 0:
            self.checkbox_vision_res = False
        self.input_len_res = self.input_len.text()
        self.input_cnt_res = self.input_cnt.text()
        f = open('settings.txt', mode='w', encoding='UTF-8')
        settings = f'{self.input_len_res}|{self.input_cnt_res}|{self.checkbox_vision_res}'
        f.write(settings)
        f.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsWindow()
    ex.show()
    sys.exit(app.exec())
