import pandas as pd
import search_images_bing as search
import os


data = pd.read_csv('PokemonData.csv')

# Getting all the Pokemons of generation 1(upto index 165)
gen1Pokemon = []
for i in range(0, 166):
    gen1Pokemon.append([data['Name'].to_list()[i],data['Type 1'].to_list()[i], data['Type 2'].to_list()[i] ])
    ''' Make directories for individual pokemon images which would be used 
    for ImageDataGenerator and for downloading Images'''
    # try:
    #     os.mkdir('dataset/test/' + gen1Pokemon[i][0])
    # except OSError:
    #     print ("Creation of the directory %s failed" % 'dataset/test/' + gen1Pokemon[i][0])
    # else:
    #     print ("Successfully created the directory %s " % 'dataset/test/' + gen1Pokemon[i][0])

def getImages(min, max):
    for i in range(min, max):
        search.search(gen1Pokemon[i][0], 'dataset/test/' + gen1Pokemon[i][0], 30)

