from concurrent.futures import ThreadPoolExecutor
from sklearn import datasets, svm
from PIL import Image
from threading import Thread
import numpy as np
import io,base64,time,socket

class Classifier:
    def __init__(self):
        # The digits dataset
        digits = datasets.load_digits()
        # To apply a classifier on this data, we need to flatten the image, to
        # turn the data in a (samples, feature) matrix:
        n_samples = len(digits.images)
        data = digits.images.reshape((n_samples, -1))
        
        # Create a classifier: a support vector classifier
        self.classifier = svm.SVC(gamma=0.001)
        
        # We learn the digits on the first half of the digits
        self.classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

    def predict(self,array:list)->list:
        return str(self.classifier.predict([array])[0])
        
def Image_processor(image_data:str)->list:
    data = image_data.split(",",1)[1]
    img_bytes = base64.b64decode(data)
    img_bytes = io.BytesIO(img_bytes)
    
    png_img = Image.open(img_bytes)
    jpg_img = png_img.convert("RGB")
    
    # Resize the image to 8x8
    resized_image = jpg_img.resize((8, 8))
    
    grayImage = resized_image.convert("P")
    array = np.round((np.array(grayImage)/255)*16)
    return array.reshape(-1)


clf = Classifier()


def main(image=None):
    if image:
        img_arr = Image_processor(image)
        return clf.predict(img_arr)
    return ""
    

if __name__ == "__main__":
    main()