from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from models.quote_model import Quote


class QuoteWidget(QLabel):
    def __init__(self) -> None:
        super(QuoteWidget, self).__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setProperty("class", "quote-label")
        self.setWordWrap(True)
        
    def set_quote(self, quote: Quote) -> None:
        self.setText(quote.text)
