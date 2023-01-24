class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_number < 12:
            self.next_question()
            self.question_number += 1
            return True
        else:
            print(f"Congratulations! You've come to the end. Your final score is {self.score}/{len(self.question_list)}.")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print(f"You got it right! Current score: {self.score}\n")
        else:
            print(f"That's wrong! Current score: {self.score}\n")

