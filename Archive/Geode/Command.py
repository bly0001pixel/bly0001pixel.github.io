import os
import pwinput
import string
import random

allCharacters = list(string.ascii_letters + string.digits + string.punctuation)

def shift_character(cipher, character, characterList):
    if character in characterList:
        originalIndex = characterList.index(character)
        shiftedIndex = (originalIndex + cipher) % len(characterList)
        return characterList[shiftedIndex]
    else:
        return character
    
def new_cipher():
    newCipher = random.randint(3, 100)

    with open("hidden/users.txt", "r") as file:
        usersData = {}
        for index, line in enumerate(file):
            if index == 0:
                oldCipher = int(line)
            else:
                lineData = line.split("=")

                passwordChars = []
                for character in lineData[1]:
                    originalCharacter = shift_character(oldCipher, character, allCharacters)
                    newCharacter = shift_character(newCipher, originalCharacter, allCharacters)
                    passwordChars.append(newCharacter)
                password = ''.join(passwordChars)

                usersData[lineData[0]] = password

    with open("hidden/users.txt", "w") as file:
        file.write(str(newCipher))
        for username, password in usersData.items():
            file.write("\n" + str(username) + "=" + str(password))

    create_users()

def read_file(filename):
    with open(filename, "r") as file:
        data = []
        indexedData = {}

        for line in file:
            data.append(line.strip())

        return data

def create_users():
    users = {}

    usersRaw = read_file("hidden/users.txt")
    cipher = int(usersRaw[0]) * -1

    for index, line in enumerate(usersRaw[1:]):
        line = line.strip()
        
        lineData = line.split("=")

        passwordChars = []
        for character in lineData[1]:
            newCharacter = shift_character(cipher, character, allCharacters)
            passwordChars.append(newCharacter)
        password = ''.join(passwordChars)

        users[lineData[0]] = password

    return users

def log_in(users, directory):
    while True:
        username = input(f"{directory}username= ")
        if username == "__RECIPHER__":
            new_cipher()
        else:
            if username in users:
                password = pwinput.pwinput(f"{directory}password:{username}= ", "*")
                if password == "__ANSWER__":
                    print(users[username])
                elif password == users[username]:
                    return username
                else:
                    print("Incorrect Password")
            else:
                print("Invalid Username")

def print_allowedCommands(allowedCommands):
    print("")
    for command in allowedCommands:
        print(command.strip(''))
    print("")

def main():
    run = True
    os.system("cls")
    users = create_users()
    directory = ">"
    loggedIn = False
    allowedCommands = ["cls", "logout", "quit", "exit", "?"]       
    
    while run:
        if not loggedIn:
            currentUser =  log_in(users, directory)
            if currentUser:
                loggedIn = True
                directory = currentUser + "> "
                os.system("cls")
            os.system("cls")

        command = input(directory)

        if command == "cls":
            os.system("cls")

        elif directory == currentUser + "> ":
            if command in allowedCommands:
                if command in ["logout"]:
                    loggedIn = False
                    directory = ">"
                    os.system("cls")
                elif command in ["quit", "exit"]:
                    os.system("cls")
                    run = False

                elif command == "?":
                    print_allowedCommands(allowedCommands)

            else:
                print("Invalid Command")

main()
new_cipher()
os.system("cls")