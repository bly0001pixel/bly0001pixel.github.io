import os, random, time
#Directory for words list
dir_path = os.path.dirname(os.path.abspath(__file__))
cwd = os.getcwd()

alphabet = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

#Time delay between gusses in seconds
delay = 1

#Minimum length for word
minLenth = 5

#Clear the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Pick answer word
def pick_word(file):
    #Open words file
    with open(file, "r") as f:
        wordsList = []

        for line in f:
            #Check if word is long enough
            if len(line) > minLenth:
                wordsList.append(line.split("\n")[0])

        #Pick random word
        answerWord = wordsList[random.randint(0,len(wordsList)-1)]

        #Turn word in to list of letters
        answerList = []
        for letter in answerWord:
            answerList.append(str.capitalize(letter))
        
        #Turn list of letters into binary for guessed status
        answerCorrect = [0 for i in range(len(answerList))]
        
        return answerWord, answerList, answerCorrect

#Display correct guesses and underscores
def display_word(answerCorrect, answerList):
    display = ""

    #Iterate through list of letters in answer word
    for index, letter in enumerate(answerCorrect):
        #If unguessed
        if letter == 0:
            display += "_ "
        #If guessed correctly
        elif letter == 1:
            display += f"{answerList[index]} "

    return display

#Initialise answer and incorrect guesses list
answerWord, answerList, answerCorrect = pick_word(os.path.join(dir_path,"words.txt"))
incorrect = []
#0 = Playing, 1 = Win, 2 = Lose
winState = 0

while True:
    cls()

    #Check if too many incorrect guesses
    if len(incorrect) > 10:
        winState = 2
        break
    #Main gameplay loop
    else:
        #Debug:
        #print(answerList)
        #print(answerCorrect)

        #Show correct and incorrect guesses
        print(f"{display_word(answerCorrect, answerList)}\n")
        print(f"Incorrect ({len(incorrect)}/10): {incorrect}")

        #Player guess
        guessLetter = str.capitalize(input("Guess: "))

        #Check if guess is a letter
        if guessLetter in alphabet and guessLetter not in incorrect:
            #Check if guess is in word
            if guessLetter in answerList:
                #Update correct letters
                for index, letter in enumerate(answerList):
                    if letter == guessLetter:
                        answerCorrect[index] = 1

                print("Correct")
                time.sleep(delay)
            else:
                #Update incorrect letters
                incorrect.append(guessLetter)

                print("Incorrect")
                time.sleep(delay)
        else:
            print("Not valid")
            time.sleep(delay)    

        #Check if all letters have been guessed
        if 0 not in answerCorrect:
            winState = 1
            break

cls()
if winState == 1:
    #Win text
    print("You Win!!!")
    print(f"The word was \"{answerWord}\"")
else:
    #Lose text
    print("You Lost :(")
    print(f"The word was \"{answerWord}\"")