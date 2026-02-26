phrase = "Go hang a salami, I'm a lasagna hog!"
phraseL = list(phrase)
exclude = ["!","@","#","$","%","^","&","*","(",")","'",'"',"-","_","+","=","{","}","[","]",":",";","<",">",",",".","?","/"]
for char in exclude:
    while char in phraseL:
        phraseL.remove(char)
phraseLL = []
for char in phraseL:
    if char not in [" ", "  "]:
        phraseLL.append(char.lower())

palindrome = True
for i in range(int(len(phraseLL)/2)):
    if phraseLL[i] == phraseLL[-(i+1)]:
        palindrome = True
    else:
        palindrome = False

print(palindrome)
