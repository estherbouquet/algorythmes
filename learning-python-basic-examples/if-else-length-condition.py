#encoding = "utf-8"

sentences = "je n'ai pas entendu mon réveil ce matin du coup, je suis en retard", "ça va ?"

for string in sentences: #pour chaque string du tableau sentences,
    if (len(string) > 15): #si la longueur de string est > 15
        print (string + " -> TL;DR") #on imprime la string + "TL;DR"
    else: #autrement
        print (string + " -> ok") #on imprime la string + "ok"


sentences = "HONDA 500 FOREMAN POWER STR. NEW 2015 !! SALE", "2015 Honda FourTrax Foreman 4x4 ES (TRX500FE1F) Work/Utility Black", "2015 Honda FourTrax Foreman 4x4 ES EPS (TRX500FE2F) Work/Utility Red", "2015 V-STAR 1300 TOURER!!! JUST PURCHASED YAMAHA FACTORY SALE!!!"
