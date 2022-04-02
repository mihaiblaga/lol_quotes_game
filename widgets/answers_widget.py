from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout
from models.answer_model import Answer
from widgets.answer_button import AnswerButton
from PyQt5.QtCore import pyqtBoundSignal, pyqtSignal


class AnswersWidget(QWidget):
    
    def __init__(self, number_of_buttons) -> None:
        super().__init__()
        self.buttons_layout = QGridLayout()
        self.answer_buttons: List[AnswerButton] = []
        self.setLayout(self.buttons_layout)
        self.number_of_buttons = number_of_buttons
        self.buid_answer_buttons(self.number_of_buttons)
        
    def buid_answer_buttons(self, number_of_buttons):
        for index in range(number_of_buttons):
            answer_button = AnswerButton()
            self.buttons_layout.addWidget(answer_button, 0, index)
            self.answer_buttons.append(answer_button)
        
    def set_answers(self, answers: List[Answer]):
        for button, answer in zip(self.answer_buttons, answers):
            button.set_answer(answer)