
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return (self.question_number + 1) <= len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        userans = input(f"Q.{self.question_number}:{current_question.text}(True/false) :").lower()
        self.check_answer(userans, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correct_answer}\nYour current score is:{self.score}/{self.question_number}\n")

        else:
            print(f"That's wrong.\nThe correct answer was: {correct_answer}\nYour current score is:{self.score}/{self.question_number}\n")