import numpy as np
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud,  STOPWORDS, ImageColorGenerator

from scipy.ndimage import gaussian_gradient_magnitude

file = open('family.txt','r') 
text=file.read()
canvas_width = 1920 # width of image
canvas_heigth = 1080 # height

steph_mask = np.array(Image.open('mask_1.jpg'))

wc = WordCloud(mask=steph_mask, colormap='inferno', random_state=5, max_font_size=50, min_font_size=0).generate(text)

# generate wordcloud
wc.to_file("simplewcloudtest3.png")

# save the output wordcloud in png format
plt.imshow(wc, interpolation='bilinear')

# show the image output
plt.axis('off')
plt.show()