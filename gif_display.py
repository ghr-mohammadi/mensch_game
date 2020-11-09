from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel


@pyqtSlot()
def gif_display(par, file, speed, length):
    disable_list = [element for element in par.btn_list if element.isEnabled()]
    par.dice_label.setHidden(True)
    for each in disable_list:
        each.setDisabled(True)

    class QMovieLabel(QLabel):
        def __init__(self, file_name, parent=None):
            super().__init__(parent)
            movie = QMovie(file_name)
            super().setMovie(movie)
            movie.setSpeed(speed)
            self.move(81, 727)
            # self.setMovie(movie)
            movie.start()

        # def setMovie(self, movie):
        #     super().setMovie(movie)
        #     movie.setSpeed(speed)
        #     self.move(81, 727)

    gif = QMovieLabel(file, par)
    gif.adjustSize()
    gif.show()

    QTimer.singleShot(length * 1000, gif.close)

    par.dice_label.setHidden(False)
    for each in disable_list:
        each.setDisabled(False)

    # start = time()

    # def thread_func(gif_file, start_time):
    #     while True:
    #         if time() - start_time > length:
    #             gif_file.close()
    #             break
    #     par.dice_label.setHidden(False)
    #     for each in disable_list:
    #         each.setDisabled(False)

    # thread_func(gif, start)

    # gif_thread = Thread(target=thread_func, args=(gif, start))
    # gif_thread.start()
    # if gif_thread.is_alive():
    #     gif_thread.join()
