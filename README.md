# Pokedex_DeepLearning
A deep learning project to identify Pokemon.
<p>Custom Dataset - 33, 358 Train and 7, 396 Test images(100*100), 166 Classes of Pokemon.</p>

# About
- Gathered custom dataset using  <b><i>Bing Search Api</i></b>  in `get_images.py` and `search_images_bing.py`
- Cleaned the downloaded images which couldn't be opened using `clean_data.py`
- Used Transfer Learning on some Pre-Trained model like <i> VGG16 </i> and <i> Mobile Net </i>
- Total Classes of Pokemon = 166

### VGG16 Model (Accuracy 51.23%)
<img src="Accuracy Charts/Vgg16 - 51.63.png">

### MobileNet Model (Accuracy 63.237%)
<img src="Accuracy Charts/MobileNet - 63.237.png">

### View Code in Kaggle
<a href="https://www.kaggle.com/mornville/pokedex/edit/run/34643259">Kaggle Notebook</a>

