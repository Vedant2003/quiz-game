class quizbrain:
  def __init__(self,q_list):
    self.question_number=0
    self.question_list=q_list
    self.score=0
  def still(self):
    return self.question_number<len(self.question_list)
  def next(self):
    current=self.question_list[self.question_number]
    self.question_number+=1
    user=input(f"q{self.question_number}:{current.text}(true/false)")
    self.check(user,current.answer)
  def check(self,user,correct):
    if user.lower()==correct.lower():
      self.score+=1
      print("You get the correct answer!")
    else:
      print("You got the wrong answer!")
      print(f"the correct answer is {correct}")
    print(f"Your correct score is:{self.score}/{self.question_number}")