"""Разработайте счетчик нажатий на кнопку, который меняет
свою надпись на число нажатий на нее (1, 2, 3 и т.д.)"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Аксенов Михаил")
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.count = 1

    def the_button_was_clicked(self):
        self.button.setText(str(self.count))
        self.count += 1


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
