from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QLabel
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        # method for widgets

    def UiComponents(self):
        # creating spin box
        self.spin = QSpinBox(self)

        # setting geometry to spin box
        self.spin.setGeometry(100, 100, 100, 40)

        #adding action to the spin box
        self.spin.valueChanged.connect(self.show_result)

       # creating label show result
        self.label = QLabel(self)

       # setting geometry
        self.label.setGeometry(100, 200, 200, 40)

       # method called by spin box

    def show_result(self):
        # getting current value
        value = self.spin.value()

        # setting value of spin box to the label
        self.label.setText("Value : " + str(value))

    # create pyqt5 app


App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
