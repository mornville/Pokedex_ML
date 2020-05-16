import pandas as pd
import search_images_bing as search
# import search_images_bing as search
data = pd.read_csv('PokemonData.csv')
# print(data.head(166))
import os

# define the name of the directory to be created

gen1Pokemon = []
# Getting all the Pokemons of generation 1(upto index 165)
for i in range(0, 166):
    gen1Pokemon.append([data['Name'].to_list()[i],data['Type 1'].to_list()[i], data['Type 2'].to_list()[i] ])
    ''' Make directories for individual pokemon images which would be used 
    for ImageDataGenerator and for downloading Images'''
    # try:
    #     os.mkdir('dataset/' + gen1Pokemon[i][0])
    # except OSError:
    #     print ("Creation of the directory %s failed" % 'dataset/' + gen1Pokemon[i][0])
    # else:
    #     print ("Successfully created the directory %s " % 'dataset/' + gen1Pokemon[i][0])

for i in range(0, len(gen1Pokemon)):
    search.search(gen1Pokemon[i][0], 'dataset/' + gen1Pokemon[i][0], 100)