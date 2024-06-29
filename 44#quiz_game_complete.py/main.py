from question_model import question
from qdata import question_data
from quiz_brain import quiz_brain
import replit
question_bank = []

for q in question_data :
    q_text = q["question"]
    q_ans = q["correct_answer"]
    new_question = question(q_text,q_ans)
    question_bank.append(new_question)

quiz = quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_q()
print(f"your final score is {quiz.score}/{quiz.q_no}")



