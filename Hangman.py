import random

def hangman():


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~ Welcome To ~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~ The Hangman Game ~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You have to guess the random country, you just have three chances for mistakes")
    print("Good luck, I hope you win!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    #alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    country = ["mexico", "china", "rusia", "guatemala", "puerto rico"]

    random_country = random.choice(country)


    guessed_letters = []
    for i in random_country:
        guessed_letters += "_"
    lifes = 3
    print(guessed_letters)
    game_on = True


    while game_on ==True:
        letter_guess = input("input a letter: ").lower()
        #letra_mayuscula = letra_minuscula.upper()
    
        
        for position in range(len(random_country)):
            letter = random_country[position]
            if letter == letter_guess:
                guessed_letters[position] =letter

                
        if (letter_guess not in random_country):
            lifes = lifes-1
            print("You got {} lifes".format(lifes))
            if lifes ==0:
                print("You're a loser!")
                break


        if "_" not in guessed_letters:
            print("The country was: {}, you are right!".format(random_country))
            print("We have a winner!")
            game_on = False
        
        print(guessed_letters)
    

hangman()

"""for i in aleatorio:
    letras_adivinadas += "_" """