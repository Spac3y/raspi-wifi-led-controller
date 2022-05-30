from mss import mss
import cv2
import numpy as np
import os
import PIL.ImageGrab

# Screen shot every 2 seconds
# Calculate the average color of the image
# Transform it into rgb values
# Send it to the led band


def get_dominant_color():
    with mss() as sct:
        # while(True):
        image = sct.shot(output = "screen.png")
        img = cv2.imread("screen.png")
        
        average = img.mean(axis=0).mean(axis=0)

        pixels = np.float32(img.reshape(-1,3))
        n_colors = 5

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS

        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels,return_counts=True)
        
        dominant = palette[np.argmax(counts)]

        return dominant

def get_average_color():
    with mss() as sct:
        image = sct.shot(output="screen.png")
        img = cv2.cvtColor(cv2.imread("screen.png"), cv2.COLOR_BGR2RGB)
        

        average_row = np.average(img,axis=0)
        average_color = np.average(average_row,axis=0)
        # average = cv2.cvtColor(average_color,cv2.COLOR_BGR2RGB)

        return average_color
        
def main():
    rgb = PIL.ImageGrab.grab().load()[1600,900]
    print(rgb)

if __name__ == '__main__':
    main()