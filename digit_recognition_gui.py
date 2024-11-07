import tkinter as tk
from tkinter import messagebox
import joblib
import os
import time
import pyscreenshot as ImageGrab
window = tk.Tk()
window.title("Handwritten Digit Recognition")
def screen_capture():
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Accessories/Paint")
    time.sleep(15)  
    images_folder = "captured_images/"
    for i in range(5):
        time.sleep(8)
        img = ImageGrab.grab(bbox=(60, 170, 400, 550))
        img.save(images_folder + str(i) + '.png')

def predict():
    model = joblib.load("model/digit_recognizer")
    images_folder = "img/"
    img = ImageGrab.grab(bbox=(60, 170, 400, 550))
    img.save(images_folder + "img.png")
    


b1 = tk.Button(window, text="1. Open Paint and Capture Screen", command=screen_capture)
b1.pack()

b2 = tk.Button(window, text="2. Predict Digit", command=predict)
b2.pack()

window.mainloop()
