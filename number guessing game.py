import random
num=random.randint(1,10)

num_guesses=0
while(num_guesses<5):
    user=int(input("welcome to the number guessing game.enter your guess from (1-10)"))
    num_guesses+=1

    if user<num:
        print("your guess is too low")
    if user>num:
        print("your guess is too high")
    if user==num:
        break

if num==user:
    print("you guessed the number in",num_guesses,"tries")
else:
    print("you couldnt guess the number.the number is",num)