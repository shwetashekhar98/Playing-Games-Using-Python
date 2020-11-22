from random_word import RandomWords
import random

r = RandomWords()
word = r.get_random_word(hasDictionaryDef="true", minLength=8, maxLength=10).lower()
#print(word)
s = random.sample(range(len(word)),len(word)//2)
#print(s)
displayed_word = ""
for w in range(len(word)):
    if w not in s or word[w].isalpha() == False :
        displayed_word += word[w]
    else:
        displayed_word += "_"

no_of_incorrect_guesses = 0

stages = [      """
                    ---------
                    |       |
                    |       O
                    |
                    |
                    |
                    |
                """,
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |
                    |
                    |
                """,
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |     -- 
                    |
                    |
                """,
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |     -- --
                    |
                    |
                """,
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |     -- --
                    |      /
                    |     /
                """,
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |     -- --
                    |      / \\
                    |     /   \\
                """,
                ]

print("\nLet's play Hangman !!\n")

print("OBJECTIVE & RULES\n")
print("Guess the word before the Hangman gets completed.")
print("Only allowed to guess Single Character at a time. Guessing more than one character in one turn is considered invalid.")
print("Each incorrect guess leads to a penalty i.e. addition of an another part in the Hangman.")
print("Maximum 6 incorrect guesses.")
print("No penalty for correct guess.\n")

print("Lets's get started !\n")

while(no_of_incorrect_guesses < 6 and displayed_word != word):
    flag=0
    for d in displayed_word:
        print(d,end=" ")
    guess = input("\n\nGuess the word (Input a missing character) : ").lower()
    if len(guess) != 1:
        print("\nInvalid Guess!! Please enter single character only.\n")
    else:
        for c in range(len(word)):
            if guess == word[c] and displayed_word[c] == "_":
                print("\nCorrect guess !!\n")
                temp = list(displayed_word)
                temp[c] = guess
                displayed_word = "".join(temp)
                flag=1
                break
        if flag == 0:
            print("\nWrong Guess !!")
            print(stages[no_of_incorrect_guesses])
            no_of_incorrect_guesses += 1
            print("No. of incorrect guesses left: %d\n"%(6-no_of_incorrect_guesses))

if displayed_word == word:
    print("You guessed the word: %s"%(displayed_word))
    print("\nCongratulations, You Won !!!")

if no_of_incorrect_guesses == 6:
    print("Sorry, You Lost.")
    print("\nThe word was %s"%(word))