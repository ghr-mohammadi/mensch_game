from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from phase_1.create_animation import login_animate
from phase_1.player import Player


class LoginDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        loadUi('login_ui.ui', self)
        self.setFixedSize(600, 320)

        self.login_btn.clicked.connect(self.is_valid)
        self.cancel_btn.clicked.connect(self.close)

    def is_valid(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()
        color = self.color_combo_box.currentText().lower()

        with open('Players_list.txt') as file:
            for line in file:
                username_, password_ = line.split()
                if username == username_ and password == password_:
                    if username not in self.parent().players.keys():
                        player = Player(username,
                                        self.parent().pieces[color],
                                        self.parent().bases[color],
                                        self.parent().positions[color])
                        self.parent().players[color] = player
                        self.color_combo_box.removeItem(self.color_combo_box.currentIndex())
                        self.parent().names[len(self.parent().players) - 1].setText(player.username)
                        self.parent().names[len(self.parent().players) - 1].setStyleSheet(
                            f"""color: {self.parent().color_code[color]};
                                border: 0 solid rgba(0,0,0,0);""")
                        login_animate(self.parent(), color)
                        if len(self.parent().players) > 1 and not self.parent().start_game.isEnabled():
                            self.parent().start_game.setEnabled(True)
                        if len(self.parent().players) > 3:
                            if self.parent().add_player in self.parent().disable_list:
                                self.parent().disable_list.remove(self.parent().add_player)
                            self.parent().add_player.setDisabled(True)
                    else:
                        QMessageBox.critical(self,
                                             'Wrong Input',
                                             'This user already exist.',
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
                    self.username_line_edit.clear()
                    self.password_line_edit.clear()
                    self.close()
                    break
            else:
                QMessageBox.warning(self,
                                    'Wrong Input',
                                    'Username or Password is incorrect.',
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)


    def combo_box_reset(self):
        self.color_combo_box.clear()
        self.color_combo_box.addItem(QIcon('ressource/game_piece_red.png'), 'Red')
        self.color_combo_box.addItem(QIcon('ressource/game_piece_blue.png'), 'Blue')
        self.color_combo_box.addItem(QIcon('ressource/game_piece_green.png'), 'Green')
        self.color_combo_box.addItem(QIcon('ressource/game_piece_yellow.png'), 'Yellow')
