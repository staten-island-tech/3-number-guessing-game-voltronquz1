





# number = 1
# while number > 0:
#     print("This will never stop!")

# order = ""

# while order != "done":
#     order = input("What would you like to order? (type 'done' to finish): ")

# print("Thanks for your order!")

colors=""
while colors != "stop":
    color=input("tell me your fav colors(type 'stop' when done)")




def guessing():
    import random
    actual=random.randint(1,10)
    guess=int(input("Guess a number from 1-10"))
    while guess !=actual:
        if guess > 10 or guess <1:
            