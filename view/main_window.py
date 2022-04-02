from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDesktopWidget
from typing import List
from models.answer_model import Answer
from widgets.answers_widget import AnswersWidget
from models.quote_model import Quote
from widgets.quote_widget import QuoteWidget


class MainWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('PyQt5 App')
        self.resize(800, 600)
        self.center()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.quote_widget = QuoteWidget()
        self.main_layout.addWidget(self.quote_widget)
        
        self.answers_widget = AnswersWidget(number_of_buttons=3)
        self.main_layout.addWidget(self.answers_widget)
        
    def center(self) -> None:
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def update_ui(self, quote: Quote, answers: List[Answer]):
        self.quote_widget.set_quote(quote)
        self.answers_widget.set_answers(answers)