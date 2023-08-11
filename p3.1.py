
import random

words_bank = [ "red" , "blue" , "black" , "pink" , "yellow" , "purple" , "green" , "white" ]
word = random.choice ( words_bank )
right_chars = []
wrong_chars = []
user_mistakes = 0

while user_mistakes < 6 :
    correct = 0
    for i in range (len (word)) :
            if word[i] in right_chars:
                   print(word[i], end=" ")
                   correct += 1
            else:
                   print("-" , end=" ")
    if correct == len(word) :
                   break
           
    user_char = input("PLease write your guess:")
    if len(user_char) == 1:
        if user_char.lower() in word :
                right_chars.append(user_char)
                print("right")
        else:
                
                wrong_chars.append(user_char)
                user_mistakes += 1
                print("wrong")
    else:
           print("Play Correctly")

if correct == len ( word ) : 
            print ("YOU WIN")

elif user_mistakes == 6 :
            print ("GAME OVER")
            print (" The word was : ", word)