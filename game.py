from random import randint

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

from phase_1.gif_display import gif_display


class Game:

    def __init__(self, parent):
        self.parent = parent
        self.parent.add_player.setDisabled(True)
        self.parent.start_game.setDisabled(True)
        self.parent.new_game.setEnabled(True)
        self.parent.roll_dice.setEnabled(True)
        self.parent.roll_dice.clicked.connect(lambda: self.onClick_roll_dice())
        self.num, self.play_dict = 0, self.parent.players
        self.color_list = [*self.parent.players.keys()]
        self.turn = self.color_list[0]
        self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
        self.parent.turn_name.setStyleSheet(
            f"""color: {self.parent.color_code[self.turn]};
                border: 0 solid rgba(0,0,0,0);""")

    def onClick_roll_dice(self):
        self.num = randint(1, 6)
        self.parent.roll_dice.setDisabled(True)

        for player in (self.play_dict[k] for k in self.play_dict.keys() if k != self.turn):
            for pic in player.pieces:
                pic.setDisabled(True)

        if self.num != 6:
            for pic in self.play_dict[self.turn].pieces:
                if pic.in_base:
                    pic.setDisabled(True)

        length = 1.3
        gif_display(self.parent, 'ressource/roll_dice.gif', 90, length)
        QTimer.singleShot(length * 1000, self.first_func)

    def first_func(self):
        self.parent.dice_label.setPixmap(QPixmap(self.parent.roll_nums[self.num]))

        if self.play_dict.keys():
            pass

        if self.play_dict[self.turn].has_move(self.num):
            pass
        else:
            if self.play_dict[self.turn].is_in_game():
                self.play_dict[self.turn].roll_num = 0
                self.turn = self.color_list[(self.color_list.index(self.turn) + 1) % len(self.color_list)]
                self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
                self.parent.turn_name.setStyleSheet(
                    f"""color: {self.parent.color_code[self.turn]};
                        border: 0 solid rgba(0,0,0,0);""")
            else:
                self.parent.roll_dice.setEnabled(True)
                if self.play_dict[self.turn].roll_num < 2:
                    self.play_dict[self.turn].roll_num += 1
                else:
                    self.play_dict[self.turn].roll_num = 0
                    self.turn = self.color_list[(self.color_list.index(self.turn) + 1) % len(self.color_list)]
                    self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
                    self.parent.turn_name.setStyleSheet(
                        f"""color: {self.parent.color_code[self.turn]};
                            border: 0 solid rgba(0,0,0,0);""")
