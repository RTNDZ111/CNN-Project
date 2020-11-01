import numpy as np
import os
from PIL import Image

class ImageLoader():

    def __init__(self):

        self.data = []
        self.labels = []

    def load_from(self, imagesPath, numberOfCategories):

        for i in range(numberOfCategories):
            path = os.path.join(os.getcwd(), imagesPath, str(i))
            images = os.listdir(path)

            print('Loading images from', path)
            
            for j in images:
                try:
                    image = Image.open(path + '\\' + j)
                    image = image.resize((30,30))
                    image = np.array(image)
                    self.data.append(image)
                    self.labels.append(i)
                except:
                    print("Error loading image")

    def get_images(self):

        return(np.array(self.data)) 

    def get_labels(self):
        
        return(np.array(self.labels))