import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

# Sample text data
text = "Vijaya ipsu dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

# Create a circular mask
#mask = np.array(Image.open("dTr6aorLc.png"))

# Create a WordCloud object with circular mask
#wordcloud = WordCloud(mask=mask, stopwords=STOPWORDS, background_color='white').generate(text_data)

# Display the word cloud using matplotlib
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis('off')
#plt.show()


# Generate a word cloud image 
stopwords = set(STOPWORDS)

mask = np.array(Image.open(r"D:\Notes\FSDS-PS\19-06-2023 Customer Review prj , ChatBot,Imp sites\Lab\dTr6aorLc.png"))
wordcloud = WordCloud(width=480, height=480,stopwords=stopwords,background_color='white', max_words=100, mask=mask,contour_color='black',contour_width=3,colormap='rainbow').generate(text)
# create image as cloud
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.show()