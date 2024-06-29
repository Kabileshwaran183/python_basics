# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1_lower=name1.lower()
n2_lower=name2.lower()
combined_string=n1_lower+n2_lower
t=combined_string.count("t")
r=combined_string.count("r")
u=combined_string.count("u")
e=combined_string.count("e")
l=combined_string.count("l")
o=combined_string.count("o")
v=combined_string.count("v")
e1=combined_string.count("e")
true=str(t+r+u+e)
love=str(l+o+v+e1)
count_str=true+love
count_int=int(count_str)
if (count_int<10 or count_int>90):
    print(f"Your score is {count_str}, "+"you go together like coke and mentos.")
elif (count_int>40 and count_int<50):
    print(f"Your score is {count_str}, "+"you are alright together.")
else:
    print(f"Your score is {count_str}.") 