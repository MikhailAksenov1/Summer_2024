"""Создайте графическое приложение с пунктами меню: Описание, Инструкция,
Помощь."""

from PyQt6.QtWidgets import (QMainWindow,QMdiArea, QApplication, QGridLayout, QPushButton, QWidget, QLineEdit, QLabel, QComboBox, QSpinBox, QDoubleSpinBox, QSlider,QGraphicsGridLayout)

import sys

class MDIWindow(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu('Меню')
        file.addAction('Описание')
        file.addSeparator()
        file.addAction('Инструкция')
        file.addSeparator()
        file.addAction('Помощь')
        file.addSeparator()

app = QApplication([])
window = MDIWindow()
window.show()
app.exec()
