import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

classifier = joblib.load('digit_recognition_model.pkl')

root = tk.Tk()
root.title("Digit Recognition Canvas")

canvas = Canvas(root, width=280, height=280, bg='white')
canvas.pack()

draw = ImageDraw.Draw(Image.new('L', (280, 280), 255))

def draw_line(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+5, y+5, fill='black', outline='black')
    draw.ellipse([x, y, x+5, y+5], fill='black')

canvas.bind("<B1-Motion>", draw_line)

def predict_digit():
    canvas_image = canvas.postscript(file='temp_canvas.ps')
    img = Image.open('temp_canvas.ps')
    img = img.convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img).flatten().reshape(1, -1)
    
    scaler = StandardScaler()
    img_array = scaler.fit_transform(img_array)
    
    prediction = classifier.predict(img_array)
    result_label.config(text=f"Prediction: {prediction[0]}")

result_label = tk.Label(root, text="Prediction: ")
result_label.pack()

predict_button = tk.Button(root, text="Predict", command=predict_digit)
predict_button.pack()

root.mainloop()
