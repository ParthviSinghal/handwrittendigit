import os
import cv2
import pandas as pd
import numpy as np

image_dir = 'images'

data = []
labels = []

for label in os.listdir(image_dir):
    label_dir = os.path.join(image_dir, label)
    if os.path.isdir(label_dir):
        for img_file in os.listdir(label_dir):
            img_path = os.path.join(label_dir, img_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (28, 28))
            img = img.flatten()
            data.append(img)
            labels.append(label)

df = pd.DataFrame(data)
df['label'] = labels

df.to_csv('dataset.csv', index=False)
