import sys

from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton, QCheckBox, QSpinBox


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.UiComponents()

    def UiComponents(self):
        # окно ввода количества особей
        self.set_cnt_spin = QSpinBox(self)
        self.set_cnt_spin.setGeometry(100, 100, 50, 25)
        self.set_cnt_spin.move(210, 45)

        # окно ввода длины особей
        self.set_len_spin = QSpinBox(self)
        self.set_len_spin.move(195, 10)
        self.set_len_spin.resize(50, 25)

    def initUI(self):
        self.setGeometry(300, 100, 260, 150)
        self.setWindowTitle('Настройки')

        # Настройка количества особей в стаде
        self.text_setting_cnt = QLabel(self)
        self.text_setting_cnt.setText('Количество особей в стаде:')
        self.text_setting_cnt.move(10, 45)
        self.text_setting_cnt.setFont(QFont('Verdana', 10))

        # Настройка длины одного животного
        self.text_len_animal = QLabel(self)
        self.text_len_animal.setText('Длина одного животного:')
        self.text_len_animal.move(10, 10)
        self.text_len_animal.setFont(QFont('Verdana', 10))

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
        self.input_len_res = self.set_len_spin.value()
        self.input_cnt_res = self.set_cnt_spin.value()
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
