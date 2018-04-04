sentence = "Bonjour tout le monde, un deux un deux, me recevez-vous ?" #maPhrase = chaîne de caractères
listOfWords = maPhrase.split() #qu'on vient découper grâce à la méthode split et qu'on vient stocker dans maListeDeMots

'''
for word in listOfWords: #pour chaque 'word' dans listOfWords,
    if 'o' in word: #s'il contient la lettre o
        print (word) #on imprime word
'''

for word in listOfWords:
    if (listOfWords.index(word) > len(listOfWords)/2): #si l'index de word dans listOfWords est > à la moitié de la longueur de la liste
        break #on arrête la boucle
    if 'u' in word: #s'il contient la lettre u
        print (word) #on imprime word
