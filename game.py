import logging
from functools import reduce
from random import randint

from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

from phase_1.gif_display import gif_display
from phase_1.finish_dialog import FinishDialog


class Game:

    def __init__(self, parent):
        self.parent = parent
        self.parent.add_player.setDisabled(True)
        self.parent.start_game.setDisabled(True)
        self.parent.new_game.setEnabled(True)
        self.parent.roll_dice.setEnabled(True)

        self.game_logger = logging.getLogger('mensch')
        self.file_handler = logging.FileHandler('mensch.log')
        self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s', datefmt='%y-%m-%d %H:%M:%S'))
        self.game_logger.setLevel(logging.INFO)
        self.game_logger.addHandler(self.file_handler)

        self.first_step()

        # self.num, self.play_dict, self.win_list = 0, self.parent.players, []
        # self.color_list = [*self.parent.players.keys()]
        # self.turn = self.color_list[0]
        # self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
        # self.parent.turn_name.setStyleSheet(
        #     f"""color: {self.parent.color_code[self.turn]};
        #         border: 0 solid rgba(0,0,0,0);""")

        self.parent.roll_dice.clicked.connect(lambda: self.onClick_roll_dice())

        for pic_list in self.parent.pieces.values():
            for pic in pic_list:
                pic.clicked.connect(lambda tmp, p=pic: self.move_piece(p))
                pic.setDisabled(True)

    def __del__(self):
        self.file_handler.close()

    def first_step(self):
        self.num, self.play_dict, self.win_list = 0, self.parent.players, []
        self.color_list = [*self.parent.players.keys()]
        self.turn = self.color_list[0]
        self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
        self.parent.turn_name.setStyleSheet(
            f"""color: {self.parent.color_code[self.turn]};
                        border: 0 solid rgba(0,0,0,0);""")

    def next_turn(self):
        self.play_dict[self.turn].roll_num = 0
        self.turn = self.color_list[(self.color_list.index(self.turn) + 1) % len(self.color_list)]
        self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
        self.parent.turn_name.setStyleSheet(
            f"""color: {self.parent.color_code[self.turn]};
                border: 0 solid rgba(0,0,0,0);""")

    def onClick_roll_dice(self):
        self.num = randint(1, 6) if self.num == 6 else 6
        self.parent.roll_dice.setDisabled(True)

        length = 1.3
        gif_display(self.parent, 'ressource/roll_dice.gif', 90, length)
        QTimer.singleShot(length * 1000, lambda: inner_func())

        def inner_func():
            nonlocal self
            self.parent.dice_label.setPixmap(QPixmap(self.parent.roll_nums[self.num]))

            move_dict = self.play_dict[self.turn].has_move(self.num)
            if reduce((lambda x, y: x or y), move_dict.values()) or self.num == 6:
                if not reduce((lambda x, y: x or y), move_dict.values()) and self.num == 6:
                    self.parent.roll_dice.setEnabled(True)
                for pic, value in move_dict.items():
                    pic.setEnabled(value)
            else:
                self.parent.roll_dice.setEnabled(True)
                if self.play_dict[self.turn].is_gamer():
                    self.next_turn()
                else:
                    if self.play_dict[self.turn].roll_num < 2:
                        self.play_dict[self.turn].roll_num += 1
                    else:
                        self.next_turn()

    def move_piece(self, pic):
        if pic.is_in_base():
            tl = 500
            self.anim = QPropertyAnimation(pic, b"geometry")
            self.anim.setDuration(tl)
            self.anim.setEndValue(self.play_dict[self.turn].positions[0].geometry())
            self.anim.start()
        else:
            tl = 250 * self.num
            pic_index = [pos.geometry() for pos in self.play_dict[self.turn].positions].index(pic.geometry())
            self.anim_grp = QSequentialAnimationGroup()
            for i in range(self.num):
                self.anim = QPropertyAnimation(pic, b"geometry")
                self.anim.setDuration(250)
                self.anim.setStartValue(self.play_dict[self.turn].positions[pic_index + i].geometry())
                self.anim.setEndValue(self.play_dict[self.turn].positions[pic_index + i + 1].geometry())
                self.anim_grp.addAnimation(self.anim)
            self.anim_grp.start()

        for pic_ in self.play_dict[self.turn].pieces:
            pic_.setDisabled(True)

        QTimer.singleShot(tl + 100, lambda: after_move())

        def after_move():
            nonlocal self, pic
            self.play_dict[self.turn].roll_num = 0

            if reduce((lambda x, y: x and y), [m.is_in_home() for m in self.play_dict[self.turn].pieces]):
                win_color = self.turn
                self.next_turn()
                self.num = 0
                # print(self.color_list)
                self.color_list.remove(win_color)
                # print(self.color_list)
                # print(self.play_dict)
                self.win_list.append((self.play_dict[win_color].username, win_color))
                del self.play_dict[win_color]
                # print(self.play_dict)
                # print(self.parent.bases)
                # print(self.parent.positions)

            if not self.play_dict:
                # print(' '.join(self.win_list))
                names = ' '.join(w[0] for w in self.win_list)
                colors = ' '.join(w[1] for w in self.win_list)
                self.win_list.clear()
                self.game_logger.info(names)
                self.parent.finish = FinishDialog(self.parent, names, colors)
                self.parent.finish.exec_()
                self.num = 0
                return
                # print('The End...')
                # QApplication.exit()

            if 0 < self.num < 6:
                self.next_turn()

            for plyr in (p for p in self.play_dict.values() if pic not in p.pieces):
                for p in plyr.pieces:
                    if pic.geometry() == p.geometry():
                        for b in plyr.bases:
                            if b.geometry() not in [m.geometry() for m in plyr.pieces]:
                                self.anim = QPropertyAnimation(p, b"geometry")
                                self.anim.setDuration(500)
                                self.anim.setEndValue(b.geometry())
                                self.anim.start()
                                QTimer.singleShot(500, lambda: self.parent.roll_dice.setEnabled(True))
                                return

            self.parent.roll_dice.setEnabled(True)
