import operator

stats = {'a':1000, 'b':3000, 'g': 100, 'd':300}
#max(sur tous les items de stats, (key), [value] )
max(stats.items(), key=operator.itemgetter(1))[0]
print(max(stats.items(), key=operator.itemgetter(1))[0]) #on affiche la key qui a la plus grande value  
