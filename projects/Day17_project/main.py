# QuizGame

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    ques = Question(question_text, question_answer)
    question_bank.append(ques)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{len(question_bank)}")