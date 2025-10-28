class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct_answer(self, answer):
        if self.correct_answer == answer:
            return True
        else:
            return False


class Quiz:
    def __init__(self):
        self.current_question_index = 0
        self.score = 0
        self.questions = [
            Question("What is the capital of France?", ["Paris", "Lyon"], "Paris"),
            Question("What is the capital of Japan?", ["Osaka", "Tokyo"], "Tokyo"),
            Question("What is the capital of Canada?", ["Toronto", "Ottawa"], "Ottawa"),
            Question("What is the capital of Australia?", ["Sydney", "Canberra"], "Canberra"),
            Question("What is the capital of Brazil?", ["Rio de Janeiro", "Brasília"], "Brasília"),
            Question("What is the capital of Germany?", ["Berlin", "Munich"], "Berlin"),
            Question("What is the capital of Italy?", ["Rome", "Milan"], "Rome"),
            Question("What is the capital of India?", ["New Delhi", "Mumbai"], "New Delhi"),
            Question("What is the capital of Egypt?", ["Cairo", "Alexandria"], "Cairo"),
            Question("What is the capital of Russia?", ["Moscow", "Saint Petersburg"], "Moscow")
        ]

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def check_answer(self, answer):
        if self.get_current_question().is_correct_answer(answer):
            self.score += 1

    def next_question(self):
        self.current_question_index += 1

    def is_finished(self):
        return self.current_question_index >= len(self.questions)

    def reset(self):
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []

# quiz = Quiz()
#
# while not quiz.is_finished():
#     question = quiz.get_current_question()
#     print(f"Question: {question.question}")
#     print("Options:", question.options)
#     answer = input("Your answer: ")
#
#     print(f"DEBUG: User answered '{answer}'")
#     quiz.check_answer(answer)
#     print(f"DEBUG: Current score = {quiz.score}")
#     quiz.next_question()
#
# print("Quiz finished!")
# print(f"Final score: {quiz.score}")
