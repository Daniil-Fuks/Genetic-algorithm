import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication, QDialogButtonBox, QVBoxLayout, QLabel

from template import template_settings_window


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        f = io.StringIO(template_settings_window)
        uic.loadUi(f, self)
        uic.loadUi('test-settings-window.ui', self)
        self.button_save.clicked.connect(self.save_settings)

    def initUI(self):
        ...

    def save_settings(self):
        if self.checkbox_vision.checkState() == 2:
            self.checkbox_vision_res = True
        elif self.checkbox_vision.checkState() == 0:
            self.checkbox_vision_res = False
        self.input_len_res = self.set_len_spin.value()
        self.input_cnt_res = self.set_cnt_spin.value()
        if int(self.input_cnt_res) * int(self.input_len_res) >= 150:
            error = CustomDialog()
            error.exec()
        self.input_loop_cnt_res = self.cnt_loop.value()
        self.input_mutation_chanse = self.mutation.value()
        f = open('settings.txt', mode='w', encoding='UTF-8')
        settings = f'{self.input_len_res};{self.input_cnt_res};{self.checkbox_vision_res};{self.input_loop_cnt_res};' \
                   f'{self.input_mutation_chanse}'
        f.write(settings)
        f.close()
        self.reject()


def execpt_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = execpt_hook
    app = QApplication(sys.argv)
    ex = SettingsWindow()
    ex.show()
    sys.exit(app.exec())


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Введены неверные значения!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
