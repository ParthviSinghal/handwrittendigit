import cv2
import csv
import glob

header = ["label"] + [f"pixel{i}" for i in range(784)]  # 28x28 = 784 pixels
with open('dataset.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(header)

for label in range(10):
    dir_list = glob.glob(f"captured_images/{label}/*.png")
    for img_path in dir_list:
        im = cv2.imread(img_path)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)
        roi = cv2.resize(im_gray, (28, 28), interpolation=cv2.INTER_AREA)

        data = [label]
        for i in range(28):
            for j in range(28):
                k = roi[i, j]
                k = 1 if k > 100 else 0  # Convert pixel values to 0 and 1
                data.append(k)

        with open('dataset.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)
