import random
from PyDictionary import PyDictionary

dictionary=PyDictionary()
from english_words import english_words_lower_alpha_set

word_list = list(english_words_lower_alpha_set)
word = random.choice(word_list)
w_list = list(word)
n = len(w_list)
blank = n*"_"
b_list = list(blank)
print("Welcome to Hangman (by Lakshya)!!")
print("Word:", blank)
print("You get 10 guesses\nLets start!")
str1 = ""
guess = 10
word_f = str1.join(b_list)
while word_f != word:
    inp = input("Enter a character: ").lower()
    if inp in w_list:
        occ = w_list.count(inp)
        for i in range(0, occ):
            index1 = w_list.index(inp)
            b_list[index1] = inp
            w_list[index1] = "_"
        word_f = str1.join(b_list)
        print(word_f)
        print("You have", guess, "guesses left")
        if guess == 0:
            print("You Lost\nThe word was", word)
            print(dictionary.meaning(word))
            break
        elif word_f == word:
            print("Congrats you WON!\nThe word was", word)
            print(dictionary.meaning(word))

    else:
        print("Try Again")
        guess -= 1
        print("You have", guess, "guesses left")
        if guess == 0:
            print("You Lost\nThe word was", word)
            print(dictionary.meaning(word))
            break
