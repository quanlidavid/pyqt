from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("PYQT6")
        self.setWindowIcon(QIcon('images/camera.png'))

        '''
        label = QLabel("Python GUI Development", self)
        # label.setText("New Text is here")
        label.move(100, 100)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet('color:red')

        # label.setText(str(12))
        label.setNum(15)
        label.clear()
        '''

        '''
        label = QLabel(self)
        pixmap = QPixmap('images/camera.png')
        label.setPixmap(pixmap)
        '''

        label = QLabel(self)
        movie = QMovie('images/bike.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
