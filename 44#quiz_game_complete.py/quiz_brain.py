class quiz_brain:
    def __init__(self,question_list):
        self.q_list= question_list
        self.q_no = 0
        self.score = 0
    
    def still_has_question(self):
        return self.q_no < len(self.q_list)

    def next_q(self):
        current_question = self.q_list[self.q_no]
        self.q_no +=1
        user_answer=input(f"Q.{self.q_no}:{current_question.q}(true/false) :")
        self.check_answer(user_answer,current_question.a)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("YOU GOT IT RIGHT")
        else :
            print("That's was wrong")
        print(f"Your current score is {self.score}/{self.q_no}")
        print("\n")

