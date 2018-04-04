#encoding = "utf-8"

sentences = "je n'ai pas entendu mon réveil ce matin du coup, je suis en retard", "ça va ?"

for string in sentences: #pour chaque string du tableau sentences,
    if (len(string) > 15): #si la longueur de string est > 15
        print (string + " -> TL;DR") #on imprime la string + "TL;DR"
    else: #autrement
        print (string + " -> ok") #on imprime la string + "ok"
