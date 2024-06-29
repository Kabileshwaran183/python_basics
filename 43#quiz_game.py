class que :
    def __init__(self,text,answer):
        self.t=text
        self.a=answer


que_1=que("2+3=5","true")
que_2=que("India is a peninsular","true")
que_3=que("venus is the third planet in our solar system","false")
que_4=que("papaya has 256 seeds in every fruit","false")
que_list=[que_1,que_2,que_3,que_4]
score=0
for i in que_list :
    print(i.t)
    ans = input("enter the answer : (true/false)").lower()
    if ans == i.a:
        print("correct answer")
        score += 1
    else:
        print("wrong answer")
    print(f"Your current score is {score}")
    print("**************************")