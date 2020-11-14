from sys import argv

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

from phase_1.create_menu import init_menu
from phase_1.game import Game
from phase_1.move_splash import MovieSplashScreen
from phase_1.set_values import set_val


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('project_ui.ui', self)

        self.game = None

        set_val(self)
        init_menu(self)

    def init_game(self):
        if not self.game:
            self.game = Game(self)
        else:
            self.add_player.setDisabled(True)
            self.start_game.setDisabled(True)
            self.new_game.setEnabled(True)
            self.roll_dice.setEnabled(True)
            self.game.first_step()


if __name__ == '__main__':
    app = QApplication(argv)

    splash = MovieSplashScreen(QMovie('ressource/dice_gif.gif'))
    splash.show()

    window = MainWindow()

    QTimer.singleShot(2500, splash.close)
    QTimer.singleShot(2500, window.show)

    app.exec_()
