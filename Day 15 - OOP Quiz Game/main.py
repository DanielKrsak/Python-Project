from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_question():
    continue

