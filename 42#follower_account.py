class user:
    def __init__(self,id,name):
        self.i = id
        self.n = name
        self.following = 0
        self.followers = 0
    
    def follow(self,user):
        user.followers +=1
        self.following +=1

user_1 = user("17","angela")
user_2 = user("28","xyz")
user_3 = user("33","iii")
user_4 = user("55","ppp")
user_5 = user("66","ooo")

user_1.follow(user_2)
user_3.follow(user_2)
user_5.follow(user_2)
user_1.follow(user_4)
user_4.follow(user_5)
user_5.follow(user_1)

list_1=[user_1,user_2,user_3,user_4,user_5]
name_1=["user_1","user_2","user_3","user_4","user_5"]
j=0
for i in list_1 :
    print(f'''{name_1[j]} : following ----> {i.following} persons
         followers ----> {i.followers} persons''')
    j +=1

