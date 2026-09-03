# name = "Yanmo"
# age = 20
# learning = "你是否正在学习 Python，是请回答true，不是回答false"
# is_learning = True
# kb = "希望成为的数据工程师/AI工程师"

# print(name)
# print(age)
# print(learning)
# print(is_learning)
# print(kb)

# print(type(name))
# print(type(age))
# print(type(learning))
# print(type(is_learning))
# print(type(kb))

"""
name = input("what's your name?")
print("hello,"+ name)
name = input("what's your age?")
print("我现在,"+ age)
is_learning = input("你是否正在学习 Python，是请回答true，不是回答false")
print("is_learning,"+ is_learning)
career_goal = input("你的学习目标是什么？")
print("学习目标：,"+ is_learning)
"""

# 类型
# name = input("What's your name? ")
# age = int(input("What's your age? "))
# is_learning = bool(input("Are you learning Python? "))
# career_goal = input("What's your career goal? ")

# #print()
# print(f"Hello, {name}!")
# print(f"You are {age} years old.")
# print(f"Are you learning Python? {is_learning}")
# print(f"Your career goal is: {career_goal}")


# #if
# s1 = bool("1")
# s2 = bool()
# s3 = bool("")
# s4 = bool(False)
# s5 = bool("false")
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)

# is_learning = bool(input("Are you learning Python? "))
# if is_learning == {"true","TRUE"}:
#     print("yes")
# else:
#     print("no")

# age = int(input("what's your age?"))
# anwser = input("are you learning python?")
# anwser = anwser.strip().lower()
# if age > 18 and anwser == "true" or anwser == "yes":
#     print("You meet the requirements.")
# else:
#     print("You don't meet the requirements.")

# if anwser == "true" or anwser == "yes" and age >= 18:
#     print("You meet the requirements.")
# else:
#     print("You don't meet the requirements.")


# age = int(input("What's your age? "))
# answer = input("Are you learning Python? ")
# answer = answer.strip().lower()
# if age >= 18 and (answer == "true" or answer == "yes"):
#     print("You meet the requirements.")
# else:
#     print("You don't meet the requirements.")

# age = int(input("What's your age? "))
# answer = input("Are you learning Python? ")
# answer = answer.strip().lower()
# if age < 18 and (answer == "true" or answer == "yes"):
#     print("Keep learning! You have plenty of time.")
# elif age < 18:
#     print("come on, day day up")
# elif age >= 18 and (answer == "true" or answer == "yes"):
#     print("Great! You are building your skills.")
# elif age >= 18:
#     print("It's never too late to start.")


users = [
    {
        "name": "Yanmo",
        "age": 20,
        "career": "Data Engineer"
    },
    {
        "name": "Alice",
        "age": 25,
        "career": "AI Engineer"
    },
    {
        "name": "Bob",
        "age": 17,
        "career": "Developer"
    }
]
for user in users:
    print(user["name"])
    
print("After loop:")
print(user["name"])
    # if user["age"] >= 18:
    #     print(user["name"])
    # if user["career"] == "AI Engineer":
    #     print(user["name"])
    # print(f"{user['name']} is {user['age'] } years old and want to be a {user['career']}")

print("I am learning Git now!test go go go")
print("3th commit")

print("I am learning Git branches!")

print("Git and Python are working together!")

print("pull test")
print("This is a fetch test!")

print("vs code to do")
print("vs code to do123")



print("I am learning Git locally!")
print("I am learning Git on GitHub!")
