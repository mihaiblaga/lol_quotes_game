from PyQt5.QtWidgets import QPushButton

from models.answer_model import Answer
from PyQt5.QtCore import pyqtBoundSignal, pyqtSignal


class AnswerButton(QPushButton):
    on_button_clicked_signal: pyqtBoundSignal = pyqtSignal(str)
    
    def __init__(self, answer: Answer = None):
        super(AnswerButton, self).__init__()
        self.clicked.connect(self.on_button_clicked)
        self.answer = answer
        
    def on_button_clicked(self):
        self.on_button_clicked_signal.emit(self.answer.text)
        
    def set_answer(self, answer: Answer):
        self.setText(answer.text)
        self.answer = answer