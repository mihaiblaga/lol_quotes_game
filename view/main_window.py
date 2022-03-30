from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDesktopWidget, QLabel
from PyQt5 import QtCore
import typing
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
        
        self.current_quote = Quote(1, 'test')
        self.quote_widget = QuoteWidget(self.current_quote)
        self.main_layout.addWidget(self.quote_widget)
        
        self.answers = None
        self.answers_widget = AnswersWidget(['test', 'test1', 'test2'])
        self.main_layout.addWidget(self.answers_widget)
        
    def center(self) -> None:
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())