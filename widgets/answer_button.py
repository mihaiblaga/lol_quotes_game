from PyQt5.QtWidgets import QPushButton

from models.answer_model import Answer


class AnswerButton(QPushButton):
    
    def __init__(self, answer: Answer):
        super(AnswerButton, self).__init__(answer)