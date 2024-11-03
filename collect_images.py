import pyscreenshot as ImageGrab
import time
import os

# Directory to save captured images
images_folder = "captured_images/0/"

for i in range(0, 100):
    time.sleep(8)  # Pausing for 8 seconds before capturing next image
    im = ImageGrab.grab(bbox=(60, 170, 400, 550))  # Coordinates (x1, y1, x2, y2)
    print(f"Saved...... {i}")
    im.save(images_folder + str(i) + '.png')
    print("Clear the screen and redraw now...")
