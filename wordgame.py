#MARCH 2023
import random
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']


def heading(text):
    print('=' * 50)
    print('|' + text.center(48) + '|')
    print('=' * 50)


def wordlist(words):
    for index,word in enumerate(words):
        print(index+1,word)


def correctwords(password,guess):
    count = 0
    for i in range(len(password)):
        if password[i] == guess[i]:
            count = count + 1
    return count


def comparewords(guess_rem):
    while guess_rem > 0: #If remaining guesses are more than 0 control enters the loop.
        print('Guesses Remaining:',guess_rem,"\n")
        guess = input('Guess(From 1-8):')
        guess_rem = guess_rem - 1 #Guess remaining reduced by 1 when user guess a word.
        try:
            user_gues = int(guess)
        except ValueError:
            print(' ')
            print('Invalid input-Enter between 1-8 only')  #If user enters other than integer this message will be printed.
            print(' ')
            continue #If user does not enter integer between 1-8 , asked again to enter valid input.
        guessed = int(user_gues)-1
        print("You guessed",'"',words[guessed],'"')
        if words[guessed] == password:  #If user guess is same as password , this loop will run.
            print('Password correct')
            print('"CONGRATULATIONS" YOU WON!')
            break
           
        else:  #If user guess is not same as password then control enters this section of if else loop.If guesses remaining will be more than 0 then if part of nested loop will run otherwise else part.            
            if guess_rem > 0:
                correctletters = correctwords(password,words[guessed]) #Correctwords function is called passing two parameters-password and guessed word.
                print('Password incorrect')
                print(correctletters,'/',len(password),'words correct\n')
                wordlist(words)  #wordlist function is called passing one parameter.
            else:
                print('Password incorrect')
                correctletters = correctwords(password,words[guessed])
                print(correctletters,'/',len(password),'words correct\n')
               
     #This loop will run if user can't guess the password with given guesses.           
    if words[guessed] != password and guess_rem == 0:
        print('You ran out of guesses')
        print('The password was','"',password,'"')



while True:  #while loop is used here so that game runs again and again until user enter n when asked to play again or not.
    heading('WELCOME TO GUESS THE WORD GAME')  #Heading function is called to print welcome message.
    print('Select difficulty level') #Prompt for difficulty level of game
    print('1.) EASY')
    print('2.) MEDIUM')
    print('3.) HARD')
    difficulty = input('You selected(enter 1-3 only):')
    if difficulty == '1':
        guess_rem = 4  #If user input for easy difficulty level 5 guesses are given to guess the password.
    elif difficulty == '2':
        guess_rem = 3  #If user input for medium difficulty level 4 guesses are given to guess the password.
    else:
        guess_rem = 2  #If user input for hard difficulty level 3 guesses are given to guess the password. 
    print('\nPassword is one of these words')
    words = random.sample(candidateWords,8)  #word_game module is used here to randomly select list of 8 words from from candidateWords which are given in word_game module.
    password = random.choice(words)  #Random password is selected at random from list of 8 words.
    wordlist(words)  #Wordlist function is called passing one parameter and is used to print list of words with their index number.
    comparewords(guess_rem)  #Comparewords function is called passing one parameter. 
    play_again = input('Do you want to play again? Y/N:').upper()
    if play_again == 'N':
        break
print('"THANK YOU FOR PLAYING"')  

