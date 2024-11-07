import joblib
import cv2
import numpy as np
import pyscreenshot as ImageGrab
model = joblib.load("model/digit_recognizer")
images_folder = "img/"

while True:
    img = ImageGrab.grab(bbox=(60, 170, 400, 500))
    img.save(images_folder + "img.png")

    im = cv2.imread(images_folder + "img.png")
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)

    ret, im_th = cv2.threshold(im_gray, 100, 255, cv2.THRESH_BINARY)
    roi = cv2.resize(im_th, (28, 28), interpolation=cv2.INTER_AREA)

    X = [1 if roi[i, j] > 100 else 0 for i in range(28) for j in range(28)]

    prediction = model.predict([X])
    print(f"Prediction: {prediction[0]}")

    cv2.putText(im, f"Prediction: {prediction[0]}", (20, 20), 0, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Result", im)
    
    if cv2.waitKey(1) == 13: 
        break

cv2.destroyAllWindows()
