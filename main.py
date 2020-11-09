from sys import argv

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

from phase_1.create_menu import init_menu
from phase_1.set_values import set_val
from phase_1.splash_display import flashSplash


class Ui(QMainWindow):
    def __init__(self, title='Mensch Game'):
        super().__init__()

        flashSplash(self, 'ressource/old_mensch.jpg', 400)
        loadUi('project_ui.ui', self)

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('ressource/dice_6.png'))
        self.setGeometry(400, 40, 1240, 980)
        self.setFixedSize(1240, 980)

        set_val(self)
        init_menu(self)


if __name__ == '__main__':
    app = QApplication(argv)
    window = Ui()
    window.show()
    app.exec_()
