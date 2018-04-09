#encoding = "utf-8"

mesOutils = ['tournevis', 'marteau', 'scie']
print (mesOutils) #affiche notre tableau
mesOutils.append('pince') #on rajoute pince à la fin de notre tableau
print (mesOutils)
mesOutils.insert(2,'crayon') #on rajoute crayon à la position 2 de notre tableau
print (mesOutils)
mesOutils[0] = 'clé à molette' #on va venir directement réécrire la string à la pos 0; tournevis devient clé à molette
print (mesOutils)
