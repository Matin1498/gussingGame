import random
from words import word_list

mlist = []
len = []
ind =[]
guessed =[]

word = random.choice(word_list)

for i in word:
    mlist.append(i)

for i in mlist:
    len.append("_")

name = input("What is your name: ")
print("Hello",name.upper()+", Welcome to my guessing game!")
tries = 10
while tries > 0:
    guess = input("\nPlease enter a character: ")
    indices = [i for i, x in enumerate(mlist) if x == guess]
    if guess in mlist:
        for i in mlist:
            if i == guess:
                for i in indices:
                    len[i] = guess
                print("Good Job",guess,"is in the word")
    elif guess in guessed:
        print("You already guessed this letter")
    elif guess not in mlist:
        guessed.append(guess)
        print("Sorry",guess,"is not in the word")
        tries -= 1
    else:
        print("Invalid Input")
    if len == mlist:
        print("\nYou won, yayyyyy")
        print("The word was",word)
        break
    if tries == 0:
        print("\nSorry", name, "you are out of guesses. You lost")
        print("The word was",word)
    print(*len, sep="")
    print("Your number of tries:", tries)




