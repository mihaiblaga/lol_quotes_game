from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

with open("champions_list.txt", 'r') as f:
    champions_list = [line.strip("\n") for line in f.readlines()]

engine = create_engine("sqlite://", echo=True)
Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    text = Column(String)
    answer_id = Column(Integer, ForeignKey('answers.id'))
    answer = relationship("Answer", back_populates="quotes")

    def __repr__(self):
        return f"<Quote(id= {self.id}, text={self.text}, answer={self.answer}>"


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    quotes = relationship("Quote", back_populates="answer")

    def __repr__(self):
        return f"<Answer(text={self.text}, quotes={self.quotes}>"


answer = Answer(text="Answer")
quote = Quote(answer_id=answer.id, text='Quote')
answer.quotes.append(quote)
print(answer)
print(quote)
