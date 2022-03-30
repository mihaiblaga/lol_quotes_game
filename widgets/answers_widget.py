from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout
from models.answer_model import Answer
from widgets.answer_button import AnswerButton


class AnswersWidget(QWidget):
    
    def __init__(self, answers) -> None:
        super().__init__()
        self.buttons_layout = QGridLayout()
        self.answers = answers
        self.build_answer_buttons(self.answers)
        self.setLayout(self.buttons_layout)
        
    def build_answer_buttons(self, answers: List[Answer]):
        for index, answer in enumerate(answers):
            answer_button = AnswerButton(answer=answer)
            self.buttons_layout.addWidget(answer_button, 0, index)