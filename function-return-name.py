#encoding = "utf-8"

def bonjour(word): #on crée une fonction qui prend comme argument le contenu de la variable word
    return word + ", " + "BONJOUR " + word.upper() + ", salut " + word.lower() + ", " + "hey "*2 + word.capitalize()
    #la fonction retourne :
    #le mot tel qu'il est rentré (avec une maj s'il y en a une)
    #le mot en majuscule (word.upper())
    #le mot en minuscule (word.lower())
    #et enfin, deux fois "hey" puis le word avec une maj au début

print (bonjour("Esther")) #on imprime ce que renvoie la fonction bonjour avec comme argument Esther
