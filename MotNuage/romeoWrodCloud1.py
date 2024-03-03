import numpy as np
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud,  STOPWORDS, ImageColorGenerator

from scipy.ndimage import gaussian_gradient_magnitude

file = open('family.txt','r') 
text=file.read()
canvas_width = 1920 # width of image
canvas_heigth = 1080 # height

# word_cloud = WordCloud(width=canvas_width, height=canvas_heigth).generate(text)

"""
 'Accent', 'Accent_r', 'Blues', 
 'Blues_r', 'BrBG', 'BrBG_r', 
 'BuGn', 'BuGn_r', 'BuPu', 
 'BuPu_r', 'CMRmap', 'CMRmap_r', 
 'Dark2', 'Dark2_r', 'GnBu', 
 'GnBu_r', 'Grays', 'Greens', 
 'Greens_r', 'Greys', 'Greys_r', 
 'OrRd', 'OrRd_r', 'Oranges', 
 'Oranges_r', 'PRGn', 'PRGn_r', 
 'Paired', 'Paired_r', 'Pastel1', 
 'Pastel1_r', 'Pastel2', 'Pastel2_r', 
 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 
 'PuBuGn_r', 'PuBu_r', 'PuOr', 
 'PuOr_r', 'PuRd', 'PuRd_r', 
 'Purples', 'Purples_r', 
 'RdBu', 'RdBu_r', 'RdGy', 
 'RdGy_r', 'RdPu', 'RdPu_r', 
 'RdYlBu', 'RdYlBu_r', 
 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 
 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 
 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 
 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 
 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 
 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 
 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 
 'cividis', 'cividis_r', 'cool', 'cool_r', 
 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 
 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 
 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 
 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 
 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 
 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 
 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 
 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 
 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 
 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 
 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 
 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 
 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', '
 tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 
 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 
 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

"""



stopwords = set(STOPWORDS)
stopwords.add('thy')
word_cloud = WordCloud(stopwords=stopwords, background_color='black', random_state=1, colormap='Blues_r', max_font_size=800, min_font_size=20, width=canvas_width, height=canvas_heigth).generate(text)


# generate wordcloud
word_cloud.to_file("simplewcloudtest2.png")

# save the output wordcloud in png format
plt.imshow(word_cloud, interpolation='bilinear')

# show the image output
plt.axis('off')
plt.show()