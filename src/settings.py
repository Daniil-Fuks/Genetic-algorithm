from PyQt5.QtWidgets import QWidget, QLabel


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
