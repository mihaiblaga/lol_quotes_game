from PyQt5.QtWidgets import QApplication, QWidget, QLabel

from models.main_model import MainModel
from .main_window import MainWindow

import typing


class MainApplication(QApplication):
    
    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)
        self.main_model = MainModel()
        self.main_window = MainWindow()
        self.main_model.update_ui_signal.connect(self.main_window.update_ui)
        self.main_model.update_model()
        self.connect_button_signals()
        self.main_window.show()

        with open('style/stylesheet.css', 'r') as f:
            self.setStyleSheet(f.read())
            
    def connect_button_signals(self):
        for answer_button in self.main_window.answers_widget.answer_buttons:
            answer_button.on_button_clicked_signal.connect(self.main_model.on_answer_button_clicked)