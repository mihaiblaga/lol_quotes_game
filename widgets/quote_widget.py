from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from models.quote_model import Quote


class QuoteWidget(QLabel):
    def __init__(self, quote: Quote) -> None:
        super(QuoteWidget, self).__init__()
        self.setText(quote.text)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setProperty("class", "quote-label")
        
    def update_quote(self, quote: Quote) -> None:
        self.setText = quote.text