import os
import pprint
import re

from models.answer_model import Answer
from models.quote_model import Quote


class QuoteProcessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_data = None

        self.champion_name = os.path.splitext(os.path.basename(file_path))[0]
        self.black_list = [self.champion_name, "Willump", "Kiko", "GG"]

    def exclude_quote_lines(self):
        with open(self.file_path, 'r', encoding='latin-1') as f:
            self.raw_data = f.readlines()
        with open(self.file_path+"_rejected", 'w', encoding='latin-1') as f_rejected,\
                open(self.file_path+"_good", 'w', encoding='latin-1') as f_good:
            for line_number, line in enumerate(self.raw_data):
                if any(black_list_item in line for black_list_item in self.black_list):
                    f_rejected.write(line)
                else:
                    f_good.write(line)

    def remove_newline_in_quote(self):
        with open(self.file_path, 'r', encoding='latin-1') as f:
            self.raw_data = f.readlines()
        with open(self.file_path, 'w', encoding='latin-1') as f:
            for line_number, line in enumerate(self.raw_data):
                if not line.endswith('"\n') and not line.endswith('*\n'):
                    line = line.replace('\n', ' ')
                    f.write(line)
                else:
                    f.write(line)

    def remove_non_quotes_from_line(self):
        with open(self.file_path, 'r', encoding='latin-1') as f:
            self.raw_data = f.readlines()
        with open(self.file_path, 'w', encoding='latin-1') as f:
            for line in self.raw_data:
                if not(line.startswith('"') or line.startswith('*')):
                    quote_index = line.find('"')
                    line = line[quote_index:]
                    f.write(line)
                else:
                    f.write(line)


with open("champions_list.txt", 'r') as f:
    champions_list = [line.strip("\n") for line in f.readlines()]

for champion in ['Nunu']:
    try:
        qp = QuoteProcessor(f"quotes/{champion}.txt")
        qp.remove_newline_in_quote()
        qp.remove_non_quotes_from_line()
        qp.exclude_quote_lines()
    except FileNotFoundError as e:
        print(e)
