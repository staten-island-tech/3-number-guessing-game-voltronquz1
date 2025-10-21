





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
randomnum=random.choice(numbers)

guessnum=int(input("guess num from 1-10"))
while guessnum != randomnum:
    if guessnum > randomnum:
        wrongnums.append(guessnum)
        print(f"The number {wrongnums} are not correct")
        print("Your number is less than the random number")
    elif guessnum < randomnum:
        wrongnums.append(guessnum)
        print(f"The number {wrongnums} are not correct")
        print("Your number is greater than the random number")
        
if guessnum ==randomnum:
        wrongnums.append(wrongnums)
        print("your number is correct")
        print("You guess correctly, the number was", randomnum)
        print("Your guess history:", wrongnums)


