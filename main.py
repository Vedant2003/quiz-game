from question_model import Question
from data import question_data
from quiz_brain import quizbrain
question_bank=[] 
for question in question_data:
  question_text=question["question"]
  question_answer=question["correct_answer"]
  new=Question(question_text,question_answer)
  question_bank.append(new)
quiz=quizbrain(question_bank)
quiz.next()
while quiz.still():
  quiz.next()
  
  