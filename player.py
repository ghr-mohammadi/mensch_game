from functools import reduce


class Player:
    # counter = 0

    def __init__(self, username, pieces, bases, positions):
        self.username = username
        self.pieces = pieces
        self.bases = bases
        self.positions = positions
        self.roll_num = 0
        for element in self.pieces:
            element.setVisible(True)
            element.set_bases(self.bases)
            element.set_positions(self.positions)
        # self.count = Player.counter
        # Player.counter += 1

    def __repr__(self):
        return self.username

    # def __del__(self):
    #     Player.counter -= 1

    def is_gamer(self):
        return reduce((lambda x, y: x or y), [p.is_in_game() for p in self.pieces])

    def has_move(self, number):
        res = {pic: False for pic in self.pieces}
        for pic in self.pieces:
            list_pics = self.pieces[:]
            list_pics.remove(pic)
            if pic.is_in_base() and number == 6 and not reduce((lambda x, y: x or y),
                                                               [p.geometry() == self.positions[0].geometry() for p in
                                                                list_pics]):
                res[pic] = True
        for pic in self.pieces:
            if pic.is_in_game() or pic.is_in_home():
                list_pics = self.pieces[:]
                list_pics.remove(pic)
                p_i = [pos.geometry() for pos in self.positions].index(pic.geometry()) + number
                if p_i < len(self.positions) and not reduce((lambda x, y: x or y),
                                                            [p.geometry() == self.positions[p_i].geometry() for p in
                                                             list_pics]):
                    res[pic] = True
        return res
