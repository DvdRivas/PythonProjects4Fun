import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {text} (True/False): "


    def get_answer(self):
        return self.current_question.answer

    def get_category(self):
        return self.current_question.category