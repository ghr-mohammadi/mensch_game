from functools import reduce


class Player:
    counter = 0

    def __init__(self, username, pieces, bases, positions):
        self.username = username
        self.pieces = pieces
        self.bases = bases
        self.positions = positions
        self.roll_num = 0
        self.step = 0
        for element in self.pieces:
            element.setVisible(True)
        self.count = Player.counter
        Player.counter += 1

    def __repr__(self):
        return self.username

    def is_in_game(self):
        return bool(reduce((lambda x, y: x + y), [not p.in_base for p in self.pieces]))

    def has_move(self, number):
        res = {pic: None for pic in self.pieces}
        for pic in self.pieces:
            list_pieces = self.pieces[:]
            list_pieces.remove(pic)
            if pic.in_base and number == 6 and not reduce((lambda x, y: x or y),
                                                          [p.geometry() == self.positions[0].geometry() for p in
                                                           list_pieces]):
                res[pic] = True
        for pic in self.pieces:
            if pic.in_game or pic.in_home:
                list_pieces = self.pieces[:]
                list_pieces.remove(pic)
                pic_index = [pos.geometry() for pos in self.positions].index(pic.geometry())
                if pic_index + number >= len(self.positions):
                    res[pic] = False
                elif not reduce((lambda x, y: x or y),
                                [p.geometry() == self.positions[pic_index + number].geometry() for p in list_pieces]):
                    res[pic] = True
                else:
                    res[pic] = False
        # print(res)
        return res
