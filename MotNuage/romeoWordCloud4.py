import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from scipy.ndimage import gaussian_gradient_magnitude

file = open("family.txt", "r")
text = file.read()
image = np.array(Image.open("mask_1.jpg"))

image_mask = image.copy()
i = image[image_mask.sum(axis=2) == 0] = 255
edges = np.mean(
    [gaussian_gradient_magnitude(image[:, :, i] / 255.0, 2) for i in range(3)], axis=0
)
image_mask[edges > 0.1] = 255
wc = WordCloud(background_color="black", mask=image_mask, mode="RGBA")
wc.generate(text)
image_colors = ImageColorGenerator(image)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation="bilinear")
wc.to_file("color_masked_wordcloud.png")
