from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup


def login_animate(parent, color):
    parent.parallel_animation_group = QParallelAnimationGroup()
    parent.anim = None
    for i in range(4):
        parent.anim = QPropertyAnimation(parent.pieces[color][i], b"geometry")
        parent.anim.setDuration(2000)
        parent.anim.setEndValue(parent.bases[color][i].geometry())
        parent.parallel_animation_group.addAnimation(parent.anim)

    parent.parallel_animation_group.start()

# def init_animate(parent):
#     parent.parallel_animation_group = QParallelAnimationGroup()
#     parent.anim_y, parent.anim_r, parent.anim_b, parent.anim_g = None, None, None, None
#     d = 2000
#     for i in range(4):
#         parent.anim_y = QPropertyAnimation(parent.pieces['yellow'][i], b"geometry")
#         parent.anim_y.setDuration(d)
#         parent.anim_y.setEndValue(parent.bases['yellow'][i].geometry())
#         parent.anim_r = QPropertyAnimation(parent.pieces['red'][i], b"geometry")
#         parent.anim_r.setDuration(d)
#         parent.anim_r.setEndValue(parent.bases['red'][i].geometry())
#         parent.anim_b = QPropertyAnimation(parent.pieces['blue'][i], b"geometry")
#         parent.anim_b.setDuration(d)
#         parent.anim_b.setEndValue(parent.bases['blue'][i].geometry())
#         parent.anim_g = QPropertyAnimation(parent.pieces['green'][i], b"geometry")
#         parent.anim_g.setDuration(d)
#         parent.anim_g.setEndValue(parent.bases['green'][i].geometry())
#         parent.parallel_animation_group.addAnimation(parent.anim_y)
#         parent.parallel_animation_group.addAnimation(parent.anim_r)
#         parent.parallel_animation_group.addAnimation(parent.anim_b)
#         parent.parallel_animation_group.addAnimation(parent.anim_g)
#
#     parent.parallel_animation_group.start()
