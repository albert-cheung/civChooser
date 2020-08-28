import random

#List of civilizations
civilizations = ["Aztecs","Berbers","Britons","Bulgarians","Burmese","Byzantines","Celts","Chinese","Cumans","Ethiopians","Franks","Goths","Huns","Incas","Indians","Italians","Japanese","Khmer","Koreans","Lithuanians","Magyars","Malay","Malians","Mayans","Mongols","Persians","Portuguese","Saracens","Slavs","Spanish","Tatars","Teutons","Turks","Vietnamese","Vikings"]

#User inputs how many people are playing
print('I hear you need help choosing civlizations for Age of Empires II. How many players need help assistance choosing a civilization?')
x = input()
if int(x) < 1:
    print("You can't have less than one player. Please uninstall the game.")
else:
    for i in range(int(x)):
        #Print random choice from civilizations list
        print('Player ' + str(int(i+1)) + ' shall play as ' + random.choice(civilizations) + '.')
