





# number = 1
# while number > 0:
#     print("This will never stop!")

# order = ""

# while order != "done":
#     order = input("What would you like to order? (type 'done' to finish): ")

# print("Thanks for your order!")

# colors=""
# while colors != "stop":
#     color=input("tell me your fav colors(type 'stop' when done)")




import random
numbers=[1,2,3,4,5,6,7,8,9,10]
wrongnums=[]
wrongnum=random.choice(numbers)

guessnum=int(input("guess num from 1-10"))
while guessnum != wrongnum:
    if guessnum > wrongnum:
        wrongnum.append(wrongnums)
        print(f"The numbers {wrongnums} are not correct")
    elif guessnum < wrongnum:
        wrongnum.append(wrongnums)
        print("Your number is greater than the random number")
    elif guessnum >wrongnum:
        print("Your number is less than the random number")
        wrongnum.append(wrongnums)
    elif guessnum ==wrongnum:
        print("your number is correct")