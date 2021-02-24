#Pseudocode Outline
#greet player
#get player name
#choose random number between 1 and 100
#repeat forever:
      #get guess
      #if guess is incorrect
        #give hint
        #increase number of guesses
      #else:
        #congratulate player

"""A number-guessing game."""

#print ('hi') # test print statement

greeting = input("Welcome to our guessing game! What is your name? > ")
greeting = greeting.title()

print(f"Hello {greeting}, guess a number between 1 and 100")