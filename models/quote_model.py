from dataclasses import dataclass

from models.answer_model import Answer


@dataclass
class Quote:
    id: int
    text: str
    answer: Answer
