from diffusers import DiffusionPipeline
import torch 
import numpy as np
import matplotlib.pyplot as plt


pipe = DiffusionPipeline.from_pretrained('stabilityai/stable-diffusion-xl-based-1.0', torch_dtype=torch.float16, use_safetensors=True, variant='ftp16')
pipe.to('cuda')

# create 4 images dor displat as output section

prompt = ["one horse sitting down the sky",
          "One boy and one girsl love each other into the sky",
          "Team of people playing football into the ocean",
          "Panda eating the moon happily"]

image1 = pipe(prompt=prompt[0]).images[0]
image2 = pipe(prompt=prompt[1]).images[0]
image3 = pipe(prompt=prompt[2]).images[0]
image4 = pipe(prompt=prompt[3]).images[0]

# create figure
fig = plt.figure(figsize=(10, 7))

rows, columns = 2,2

# adds a supplot at the 1st position
fig.add_subplot(rows, columns, 1)

#showing the first image
plt.imshow(image1)
plt.axis('off')
plt.title(prompt[0])

# adds a supplot at the 1st position
fig.add_subplot(rows, columns, 2)

#showing the 2 image
plt.imshow(image2)
plt.axis('off')
plt.title(prompt[1])

# adds a supplot at the 1st position
fig.add_subplot(rows, columns, 3)

#showing the first image
plt.imshow(image3)
plt.axis('off')
plt.title(prompt[2])

# adds a supplot at the 1st position
fig.add_subplot(rows, columns, 4)

#showing the first image
plt.imshow(image4)
plt.axis('off')
plt.title(prompt[3])


#  savinf Image locally
image1.save(prompt[0]+"png")
image2.save(prompt[1]+"png")
image3.save(prompt[2]+"png")
image4.save(prompt[3]+"png")




