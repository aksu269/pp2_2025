import random
correct_num = random.randint(1, 21)
name = input('Hello! What is your name?\n')
num = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))
cnt = 0
while True:
    if num < correct_num:
        num = int(input('Your guess is too low. \nTake a guess.\n'))
    elif num > correct_num:
        num = int(input('Your guess is too low.\nTake a guess.\n'))
    else:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    cnt += 1
