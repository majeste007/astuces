
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = open('fam.txt','r') 
text=file.read()
canvas_width = 1920 # width of image
canvas_heigth = 1080 # height

word_cloud = WordCloud(width=canvas_width, height=canvas_heigth, colormap='Blues_r').generate(text)

# generate wordcloud
word_cloud.to_file("goalWordCloud1.png")

# save the output wordcloud in png format
plt.imshow(word_cloud, interpolation='bilinear')

# show the image output
plt.axis('off')
plt.show()


