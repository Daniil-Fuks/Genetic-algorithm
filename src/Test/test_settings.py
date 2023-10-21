from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class DialogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 350, 200)
        self.setWindowTitle('Настройки')

        self.text_setting_cnt = QLabel(self)
        self.text_setting_cnt.setText('Количество особей в стаде:')
        self.text_setting_cnt.move(10, 10)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        line1 = QPainter()
        # Начинаем процесс рисования
        line1.begin(self)
        self.draw_line1(line1)
        # Завершаем рисование
        line1.end()

    def draw_line1(self, line):
        # Задаем кисть
        line.setBrush(QColor(255, 0, 0))
        # Рисуем прямоугольник заданной кистью
        line.drawLine(20, 30, 140, 30)