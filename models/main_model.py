from models.answer_model import Answer
from models.quote_model import Quote
from typing import List
from PyQt5.QtCore import pyqtBoundSignal, pyqtSignal, QObject
import random


class MainModel(QObject):
    
    update_ui_signal: pyqtBoundSignal = pyqtSignal(object, object)
    
    def __init__(self) -> None:
        super(MainModel, self).__init__()
        
        self.quotes: List[Quote] = None
        self.load_quotes_from_file(None)
        
        self.used_quotes_ids: List[Quote.id] = []
        
        self.possible_answers_list: List[Answer] = None
        self.load_answers_from_file("/home/mihaiblaga/lol_quotes_game/raw_data.txt")
        
        self.current_answers: List[Answer] = None
        self.current_quote: Quote = None
        
        
        
    def on_answer_button_clicked(self, answer):
        if self.current_quote.answer.text == answer:
            self.correct_answer_clicked()
        else:
            print('Bad')
            
    def correct_answer_clicked(self):
        self.used_quotes_ids.append(self.current_quote.id)
        self.update_model()
        # TODO score
        
    def wrong_answer_clicked(self):
        print("wrong answer")
        
    def get_random_quote(self):
        random_quote = random.choice(self.quotes)
        if self.current_quote:
            if random_quote.id in self.used_quotes_ids:
                return self.get_random_quote()    
            else:
                return random_quote   
        return random_quote
             
            
    def set_quote(self, quote):
        self.current_quote = quote
    
    def set_answers(self, answers):
        self.current_answers = answers
        
    def load_answers_from_file(self, file_path):
        with open(file_path, 'r') as f:
            self.possible_answers_list = [Answer(line.strip('\n')) for line in f.readlines()]
            
    def load_quotes_from_file(self, file_path):
        self.quotes = [Quote(1, 'Aatrox is answer', Answer('Aatrox')),
                Quote(2, 'Lux is answer', Answer('Lux')),
                Quote(3, 'Ahri is answer', Answer('Ahri'))]
        
    def update_model(self):
        next_quote = self.get_random_quote()
        answers = self.get_random_answers(2)
        answers.append(next_quote.answer)
        random.shuffle(answers)
        self.set_quote(next_quote)
        self.set_answers(answers)
        self.update_ui_signal.emit(self.current_quote, self.current_answers)
        
    def get_random_answers(self, amount: int) -> List[Answer]:
        return random.choices(self.possible_answers_list, k=amount)