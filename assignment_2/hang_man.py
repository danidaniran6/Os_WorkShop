import random
words_bank=["book","apple","sadjad","mashhad","blue","tree","linux","iran","python","comuter"]
word=random.choice(words_bank)
user_true_chars=[]
user_word =""
joon=5

while (True):

    user_word = ""
    for i in range(len(word)):
        if word[i] in user_true_chars:
            print(word[i], end="")
            user_word+=word[i]
        else:
            print("_", end="")
            user_word+="_"
    if user_word==word :
           print("\n","باریکلا")
           break
    print("\nplease enter a character:")
    user_char=input()
    if len(user_char)==1:
        if user_char in word:
            user_true_chars.append(user_char)
            position = word.find(user_char)
            print("correct")
        else:
            joon -= 1
            print("wrong")
        if  joon==0:
            print("Game over")
            break

        #shart bord?
        elif user_word==word :
           print("باریکلا")
           break
    else:
        print("mese adam vared kon :|")