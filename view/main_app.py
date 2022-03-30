from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from .main_window import MainWindow

import typing


class MainApplication(QApplication):
    
    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)
        self.main_window = MainWindow()
        self.main_window.show()

        with open('style/stylesheet.css', 'r') as f:
            self.setStyleSheet(f.read())