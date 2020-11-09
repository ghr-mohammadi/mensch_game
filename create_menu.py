from PyQt5.QtWidgets import QApplication

from phase_1.game import Game
from phase_1.login_dialog import LoginDialog


def init_menu(parent):
    parent.add_player.triggered.connect(LoginDialog(parent).exec_)
    parent.add_player.setShortcut('Ctrl+P')
    parent.add_player.setStatusTip('Game \u2192 Add Player')

    parent.start_game.triggered.connect(lambda: Game(parent))
    parent.start_game.setShortcut('Ctrl+G')
    parent.start_game.setStatusTip('Game \u2192 Start Game')
    parent.start_game.setDisabled(True)

    parent.new_game.triggered.connect(lambda: print('New Game'))
    parent.new_game.setShortcut('Ctrl+N')
    parent.new_game.setStatusTip('Game \u2192 New Game')
    parent.new_game.setDisabled(True)

    parent.exit_game.triggered.connect(QApplication.exit)
    parent.exit_game.setShortcut('Ctrl+Q')
    parent.exit_game.setStatusTip('Game \u2192 Exit')

    parent.status_bar.showMessage('Welcome To Mensch Game')

    parent.roll_dice.setDisabled(True)
