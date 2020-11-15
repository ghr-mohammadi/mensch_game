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
