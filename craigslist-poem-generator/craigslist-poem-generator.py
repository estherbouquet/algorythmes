import operator
import nltk
import nltk.data
import random
import json
from nltk.corpus import stopwords

annonces = None

with open('gigs.json', 'r', encoding="utf8") as fichier:
  annonces = json.loads(fichier.read())

print(annonces)
'''
#on crée un tableau qui contient nos annonces
annonces = [
    {"body":"\n        \n            QR Code Link to This Post\n            \n        \nHi,\n\nI am seeking a middle man, (Manager or Beat Broker) to assist in placing, selling, and publishing my tracks. I also am a highly skilled Engineer and am looking for work.\n\nA few of my qualifications are:\n\n-Music Producer, Track Composer, Recording Engineer, Instrumentalist\n-15+ years of experience working with independent artists and some major artists\n-Specialize in Urban and Pop Music\n-Work remotely from my own studio and I'm Pro Tools Certified\n-Hold my College Degree in Music Production and Recording Engineering\n-Personally mentored by the late great MC Breed\n-I am the cousin of industry leader Gerry Lacoursiere (Founder/President A&M Canada)\n\nPlease see my website for more: https://www.ckrepertoire.com\n\nThank you for your time and consideration. I look forward to hearing from you.\n\n-----Kevin    ",
    "title":"-----Beat Composer/Producer Seeks Song Plugger/Manager-----",
    "url":"https://newyork.craigslist.org/brk/muc/d/beat-composer-producer-hip/6551898948.html"},
    {"body":"\n        \n            QR Code Link to This Post\n            \n        \nLooking for a young experienced eager trim athletic in shape plumbers helper with a big wrench in his tool kit. Must be comfortable getting down and dirty and laying back in tight spaces for a good job to get done. Don't be timid or afraid to show me whats what inside the tank and how it works. Experience with snake outs not necessary but always a plus. Opportunity to grow for the right guy.    ",
    "title":"Looking a Young 19yo- 29yo Experienced Plumbers Helper",
    "url":"https://newyork.craigslist.org/que/act/d/looking-for-young-19yo-29yo/6551850469.html"}
]
'''


#freq est un dictionnaire :
# freq = {"mot": {count : 4, "annonces" : []}}
freq = {}

#maxfreq = {"count": -10000,"annonce":{} } #-> doit me donner le mot (du genre "le") sauf que ça retourne qu'un entier
#on choisit donc de crér un entier à -10000
maxfreq = -10000
#et on initialise leMot avec rien à l'intérieur
leMot = ""
counter = 0
listeDesAnnoncesSelectionnees = []
annoncesAvecMotIdentique = []
phrasesSelectionneesPourPoeme = []

#PREMIERE BOUCLE POUR CHERCHER LE MOT QUI REVIENT LE PLUS (AVEC SON NOM ET SON NOMBRE) :

for annonce in annonces: #pour chaque annonce dans le tableau annonces
    motstemp = annonce["title"].split() #on vient stocker les mots découpés du titre de l'annonce ans la liste mots
    mots = [word for word in motstemp if word not in stopwords.words('english')]

    for mot in mots: #et pour chaque mot dans notre liste de mots
    #penser à faire un lower quelque part
        mot = mot.lower()
        if mot in freq: #si le mot est dans notre dictionnaire
            freq[mot]["count"]+=1 #on incrémente notre compteur de 1
            freq[mot]["annonces"].append(annonce) #et on ajoute l'annonce complète dans annonces

            if freq[mot]["count"] > maxfreq: #si le count et sup à maxfreq
                maxfreq = freq[mot]["count"] #maxfreq prend la valeur de "count"
                leMot = mot #et on remplit la chaîne de char leMot avec le "mot" qu'on regarde via la boucle

        else: #autrement,
            freq[mot] = {} #o crée un dictionnaire vide pour le nouveau mot
            freq[mot]["count"] = 1 #on initialise la valeur de count à 1
            freq[mot]["annonces"] = [annonce] #on rajoute annonces dans le tableau d'annonce du mot
    print("mot : ", leMot, " - récurrence : ", freq[mot]["count"]) #imprime toutes les valeurs des counts c-à-d, le nombre de fois où un même mot revient

#print(freq) #imprime tout le dictionnaire
print()
print("mot : ", leMot, " | récurrence : x", maxfreq) #imprime le nombre max et le mot


#DEUXIEME BOUCLE POUR RETROUVER LES ANNONCES QUI ONT CE MOT DANS LEUR TITRE POUR LES STOCKER AILLEURS :

for annonce in annonces: #pour chaque annonce dans le tableau annonces
    mots = annonce["title"].split()
    if leMot in mots:
        counter = counter+1
        #print(counter, annonce["title"])
        #print(annonce["body"])
        listeDesAnnoncesSelectionnees.append(annonce["body"])
print()
print("ma liste hourra lala : ", listeDesAnnoncesSelectionnees)

finding_sentences = nltk.data.load('tokenizers/punkt/english.pickle')

for lines in listeDesAnnoncesSelectionnees: #pour chaque ligne de ma liste listeDesAnnoncesSelectionnees,
    # this returns a list with 1 element containing the entire text, sentences separated by \n
    #genre grosse chaîne de char
    sentences = '\n'.join(finding_sentences.tokenize(lines.strip()))
    print()
    print("sentences : ", sentences)

    # transform string into list of sentences -> par annonce vu qu'on est dans la boucle
    sentences_list = sentences.split("\n")
    print()
    print("sentences_list : ", sentences_list)
    #il faut donc les envoyer dans une liste mère qui contiendra toutes les annonces dont le titre contient le mot clef
    #sur laquelle il faudra faire un random.choice

    annoncesAvecMotIdentique.append(sentences_list)

for annonce in annoncesAvecMotIdentique:
    phrase = random.choice(annonce)
    phrasesSelectionneesPourPoeme.append(phrase)
#print()
#print("----")
#print("mon joli poème : ")
#print(phrasesSelectionneesPourPoeme)
#print("----")

file = open('testfile.txt', 'a')

print()
print("----")
print("mon joli poème : ")
print("titre :", leMot)

file.write(leMot)
file.write('\n')
file.write("----")
file.write('\n')
for phrase in phrasesSelectionneesPourPoeme:
    vers = '\n'.join(finding_sentences.tokenize(phrase.strip())) #export en chaîne de char olé
    print(vers)
    file.write(vers)
    file.write('\n')

file.write("----")
file.write('\n')
file.write('\n')

print("----") #bouyaaa

file.close()


#pour trouver la plus grande valeur ?
#max(iterable, *[, key, default])
#max(freq.items(), key=operator.itemgetter(1))[0]
#print(max(freq.items(), key=operator.itemgetter(1))[0])

#TO-DO :
#-> comment imprimer juste le mot et le nombre de fois où il revient ? OK
#-> comment importer directement notre JSON ?

#-> comment trouver la plus grande valeur ? -> dans l'idéal, les trois + grandes mais tant pis OK
#-> une fois qu'on a trouvé les 3 mots principaux, on en fait une string
#-> et on prend les annonces correspondantes dans lesquelles on lance un random sur leurs strings
#-> qu'on combine ensemble pour faire un tableau ? ou une chaîne de char
