# word guess game 
import random

mywords = ["apple", "bat", "cat", "dog", "egg", "fox", "gun", "house", "ink", "jug",
           "kite", "lamp", "map", "night", "owl", "pen", "queen", "rat", "sun",
           "tank", "umbrella", "van", "wall", "xerox", "young", "zoo"]

word = random.choice(mywords)
guessword = ["_"] * len(word)

l = int(input("Choose level: 1.hard / 2.medium / 3.easy\n"))

if l == 1:
    attempts = 8
elif l == 2:
    attempts = 9
else:
    attempts = 10

total_attempts = attempts  


print("Your word starts with:", word[0])

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessword))
    guess = input("Guess letter of the word: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessword[i] = guess
        print(" Good going")
    else:
        attempts -= 1
        print(" Try again, you have", str(attempts), "attempts left.")

    if "_" not in guessword:
        print("\nCongratulations! You have guessed the word:", word)
        score = (total_attempts - attempts) * 100
        print("Your score is:", score)
        if m < score:
            m = score
        print("Highest score is:", m)
        break

else:
    print("\n You are out of chances. The word is:", word)