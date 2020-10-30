import tensorflow.keras as tfk
import tensorflow as tf
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import time
import numpy as np
import cv2
#import pyfakewebcam
import pyvirtualcam
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.config.experimental.set_visible_devices([], 'GPU')
print(tf.config.experimental.list_physical_devices('GPU'))
print(tf.config.experimental.list_logical_devices('GPU'))


class MainWindow():
    # def __init__(self, window, classes, model, cap, virtualCamera):
    # def __init__(self, window, classes, model, cap):
    def __init__(self, window, classes, model, cap, cam):
        self.window = window
        self.classes = classes
        self.model = model
        self.cap = cap
        pad = 3
        #self.virtualCamera = virtualCamera
        self.cam = cam
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        print(self.width, self.height)
        self.window.geometry(
            "{0}x{1}+0+0".format(self.width-pad, self.height-pad))
        self.alpha = 0.1
        self.window.wait_visibility(self.window)
        self.window.wm_attributes('-alpha', self.alpha)
        self.window.iconify()
        self.interval = 20  # Interval in ms to get the latest frame
        self.line = []

        # Create canvas for image
        self.canvas = tk.Canvas(
            self.window, width=self.width, height=self.height)
        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.canvas.bind("<Button-1>", self.xySTART)
        self.canvas.bind("<B1-Motion>", self.addLine)
        self.canvas.bind('<ButtonRelease-1>', self.xyEND)
        self.i = 0
        self.period = 0

        # Update image on canvas
        self.update_image()

    def update_image(self):

        # disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Create the array of the right shape to feed into the keras model.
        # We are inputting 1x 224x224 pixel RGB image.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # capture image
        check, frame = self.cap.read()
        # mirror image - mirrored by default in Teachable Machine
        # depending upon your computer/webcam, you may have to flip the video
        # frame = cv2.flip(frame, 1)

        # crop to square for use with TM model
        margin = int(((frameWidth-frameHeight)/2))
        square_frame = frame[0:frameHeight, margin:margin + frameHeight]
        # resize to 224x224 for use with TM model
        resized_img = cv2.resize(square_frame, (224, 224))
        # convert image color to go to model
        model_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

        # turn the image into a numpy array
        image_array = np.asarray(model_img)
        # normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # load the image into the array
        data[0] = normalized_image_array

        # run the prediction
        predictions = self.model.predict(data)

        # confidence threshold is 90%.
        conf_threshold = 70
        confidence = []

        # for each one of the classes
        for i in range(0, len(self.classes)):
            # scale prediction confidence to % and apppend to 1-D list
            confidence.append(int(predictions[0][i]*100))

        print(confidence)
        if confidence[1] > conf_threshold:
            if self.i < 11:
                self.i += 1
        else:
            if self.i > 0:
                self.i -= 1

        if self.period <= 10:
            self.period += 1
        else:
            self.period = 0
            if self.i == 11 and self.alpha <= 0.1:
                self.window.deiconify()
                self.increaseTransparency()
            elif self.i == 0 and self.alpha >= 1:
                self.decreaseTransparency()
                self.window.iconify()

        self.pano = Image.new(
            "RGBA", (self.width, self.height), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.pano)
        if self.line:
            pX = self.line[0][0]
            pY = self.line[0][1]
            for i in range(len(self.line)):
                alpha = time.time() - self.line[i][2]
                self.line[i][3] = int(255 - alpha*85)
                # print(alpha)
                if self.line[i][0] != -1:
                    self.draw.line([(pX, pY), (self.line[i][0], self.line[i][1])],
                                   fill=(255, 0, 255, self.line[i][3]), width=10)
                    pX = self.line[i][0]
                    pY = self.line[i][1]
                elif i+1 < len(self.line):
                    pX = self.line[i+1][0]
                    pY = self.line[i+1][1]
            if self.line[0][3] <= 0:
                self.line.pop(0)
        # send to virtual webcam
        camIMG = np.array(self.pano)
        # self.virtualCamera.schedule_frame(camIMG)
        # Get the latest frame and convert image format
        self.pano = ImageTk.PhotoImage(self.pano)  # to ImageTk format

        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.pano)

        # Repeat every 'interval' ms
        print("Cam send")
        self.cam.send(camIMG)
        self.cam.sleep_until_next_frame()
        self.window.after(self.interval, self.update_image)

    def increaseTransparency(self):
        while self.alpha < 1:
            self.alpha += 0.15
            self.window.wm_attributes('-alpha', self.alpha)
            self.window.update_idletasks()
            self.window.update()
            time.sleep(0.1)

    def decreaseTransparency(self):
        while self.alpha > 0.1:
            self.alpha -= 0.15
            self.window.wm_attributes('-alpha', self.alpha)
            self.window.update_idletasks()
            self.window.update()
            time.sleep(0.1)

    def xySTART(self, event):
        tmp = [event.x, event.y, time.time(), 255]
        self.line.append(tmp)

    def addLine(self, event):
        tmp = [event.x, event.y, time.time(), 255]
        self.line.append(tmp)

    def xyEND(self, event):
        tmp = [-1, -1, time.time(), 255]
        self.line.append(tmp)


if __name__ == "__main__":
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    #virtualCamera = pyfakewebcam.FakeWebcam('/dev/video2', width, height)
    # read .txt file to get labels
    labels_path = "converted_keras/labels.txt"
    # open input file label.txt
    labelsfile = open(labels_path, 'r')

    # initialize classes and read in lines until there are no more
    classes = []
    line = labelsfile.readline()
    while line:
        # retrieve just class name and append to classes
        classes.append(line.split(' ', 1)[1].rstrip())
        line = labelsfile.readline()
    # close label file
    labelsfile.close()

    # load the teachable machine model
    model_path = 'converted_keras/keras_model.h5'
    model = tfk.models.load_model(model_path, compile=False)

    # initialize webcam video object
    cap = cv2.VideoCapture(0)

    # width & height of webcam video in pixels -> adjust to your size
    # adjust values if you see black bars on the sides of capture window
    frameWidth = 1280
    frameHeight = 720

    # set width and height in pixels
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)
    # enable auto gain
    cap.set(cv2.CAP_PROP_GAIN, 0)
    cam = pyvirtualcam.Camera(
        width=width, height=height, fps=20)
    MainWindow(root, classes, model, cap, cam)
    #MainWindow(root, classes, model, cap)
    #MainWindow(root, classes, model, cap, virtualCamera)
    root.mainloop()
