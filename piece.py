from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton


class Piece(QPushButton):
    def __init__(self, parent, color, n):
        super().__init__(parent)
        self.setGeometry(410, 410, 69, 69)
        self.__icon = QIcon()
        self.__icon.addPixmap(QPixmap(f'ressource/game_piece_{color}.png'), QIcon.Normal)
        self.__icon.addPixmap(QPixmap(f'ressource/game_piece_{color}_disabled.png'), QIcon.Disabled)
        self.setIcon(self.__icon)
        self.setIconSize(QSize(69, 69))
        self.setStyleSheet("""border-color: rgba(255, 255, 255, 0);
                              background-color: rgba(255, 255, 255, 0);""")
        self.color = color
        self.name = color + '_' + str(n)
        self.setVisible(False)
        self.in_base = True
        self.in_game = False
        self.in_home = False

    def __repr__(self):
        return self.name
