from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton


class Piece(QPushButton):
    def __init__(self, parent, color, n):
        super().__init__(parent)
        self.setDisabled(True)
        self.setVisible(False)
        self.setGeometry(410, 410, 69, 69)

        self.__icon = QIcon()
        self.__icon.addPixmap(QPixmap(f'ressource/game_piece_{color}.png'), QIcon.Normal)
        self.__icon.addPixmap(QPixmap(f'ressource/game_piece_{color}_disabled.png'), QIcon.Disabled)
        self.setIcon(self.__icon)
        self.setIconSize(QSize(69, 69))
        self.setStyleSheet("""border-color: rgba(255, 255, 255, 0);
                              background-color: rgba(255, 255, 255, 0);""")

        self.color = color
        self.setStatusTip(self.color.capitalize() + ' Piece')
        self.name = color + '_' + str(n)
        self.__bases, self.__positions = None, None

    def __repr__(self):
        return self.name

    def set_bases(self, bases):
        self.__bases = bases

    def set_positions(self, positions):
        self.__positions = positions

    def is_in_base(self):
        return self.geometry() in [base.geometry() for base in self.__bases]

    def is_in_game(self):
        return self.geometry() in [position.geometry() for position in self.__positions[:-4]]

    def is_in_home(self):
        return self.geometry() in [position.geometry() for position in self.__positions[-4:]]
