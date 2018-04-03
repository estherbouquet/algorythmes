#encoding = "utf-8"

# pour exe notre fichier :
# aller dans dossier de notre projet via terminal
# puis rentrer python nomdemonficher.py
# -> lancer avec python3 au lieu de python pour une meilleure gestion des accents

print("tadaa") #hello est considere comme une String et non comme une valeur ou une fonction
print("olé"+" "+"caliente") #va agreger les mots ensemble

mot1 = "ah ouhh" #variable
mot2 = "tcha "

print(mot1, mot2*3)
print("-----")


def bonjour(word): #on crée une fonction qui prend comme argument le contenu de la variable word
    return word + ", " + "BONJOUR " + word.upper() + ", salut " + word.lower() + ", " + "hey "*2 + word.capitalize()
    #la fonction retourne :
    #le mot tel qu'il est rentré (avec une maj s'il y en a une)
    #le mot en majuscule (word.upper())
    #le mot en minuscule (word.lower())
    #et enfin, deux fois "hey" puis le word avec une maj au début

print (bonjour("Esther")) #on imprime ce que renvoie la fonction bonjour avec comme argument Esther
