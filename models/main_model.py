from models.answer_model import Answer
from models.quote_model import Quote
from typing import List
from PyQt5.QtCore import pyqtBoundSignal, pyqtSignal, QObject
import random


class MainModel(QObject):
    
    update_ui_signal: pyqtBoundSignal = pyqtSignal(object, object)
    
    def __init__(self) -> None:
        super(MainModel, self).__init__()
        
        self.quotes: List[Quote] = []
        self.load_quotes_from_file('quotes/Aatrox.txt_good')
        random.shuffle(self.quotes)
        
        self.used_quotes_ids: List[Quote.id] = []
        
        self.possible_answers_list: List[Answer] = []
        self.load_answers_from_file("champions_list.txt")
        
        self.current_answers: List[Answer] = []
        self.current_quote: Quote = None

    def on_answer_button_clicked(self, answer):
        if self.current_quote.answer.text == answer:
            self.correct_answer_clicked()
        else:
            self.wrong_answer_clicked()
            
    def correct_answer_clicked(self):
        self.used_quotes_ids.append(self.current_quote.id)
        self.update_model()
        # TODO score
        
    def wrong_answer_clicked(self):
        print("wrong answer")
        
    def get_quote(self):
        if self.quotes:
            return self.quotes.pop(0)
        else:
            return Quote(None, 'No more quotes', Answer(''))

    def set_quote(self, quote):
        self.current_quote = quote
    
    def set_answers(self, answers):
        self.current_answers = answers
        
    def load_answers_from_file(self, file_path):
        with open(file_path, 'r') as f:
            self.possible_answers_list = [Answer(line.strip('\n')) for line in f.readlines()]
            
    def load_quotes_from_file(self, file_path):
        with open(file_path, 'r') as f:
            raw_quotes = f.readlines()
        self.quotes = [Quote(index, raw_quote, Answer("Aatrox")) for index, raw_quote in enumerate(raw_quotes)]
        
    def update_model(self):
        next_quote = self.get_quote()
        answers = self.get_random_answers(2)
        answers.append(next_quote.answer)
        random.shuffle(answers)
        self.set_quote(next_quote)
        self.set_answers(answers)
        self.update_ui_signal.emit(self.current_quote, self.current_answers)
        
    def get_random_answers(self, amount: int) -> List[Answer]:
        return random.choices(self.possible_answers_list, k=amount)
