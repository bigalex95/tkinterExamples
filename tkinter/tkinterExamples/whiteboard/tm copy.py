# Easy Machine Learning & Object Detection with Teachable Machine
#
# Michael D'Argenio
# mjdargen@gmail.com
# https://dargenio.dev
# https://github.com/mjdargen
# Created: February 6, 2020
# Last Modified: February 6, 2020
#
# This program uses Tensorflow and OpenCV to detect objects in the video
# captured from your webcam. This program is meant to be used with machine
# learning models generated with Teachable Machine.
#
# Teachable Machine is a great machine learning model trainer and generator
# created by Google. You can use Teachable Machine to create models to detect
# objects in images, sounds in audio, or poses in images. For more info, go to:
# https://teachablemachine.withgoogle.com/
#
# For this project, you will be generating a image object detection model. Go
# to the website, click "Get Started" then go to "Image Project". Follow the
# steps to create a model. Export the model as a "Tensorflow->Keras" model.
#
# To run this code in your environment, you will need to:
#   * Install Python 3 & library dependencies
#       * Follow instructions for your setup
#   * Export your teachable machine tensorflow keras model and unzip it.
#       * You need both the .h5 file and labels.txt
#   * Update model_path to point to location of your keras model
#   * Update labels_path to point to location of your labels.txt
#   * Adjust width and height of your webcam for your system
#       * Adjust frameWidth with your video feed width in pixels
#       * Adjust frameHeight with your video feed height in pixels
#   * Set your confidence threshold
#       * conf_threshold by default is 90
#   * If video does not show up properly, use the matplotlib implementation
#       * Uncomment "import matplotlib...."
#       * Comment out "cv2.imshow" and "cv2.waitKey" lines
#       * Uncomment plt lines of code below
#   * Run "python3 tm_obj_det.py"

import multiprocessing
import numpy as np
import cv2
import tensorflow.keras as tf
import pyttsx3
import math

# main line code
# if statement to circumvent issue in windows
if __name__ == '__main__':

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
    model = tf.models.load_model(model_path, compile=False)

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

    # keeps program running forever until ctrl+c or window is closed
    while True:

        # disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Create the array of the right shape to feed into the keras model.
        # We are inputting 1x 224x224 pixel RGB image.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # capture image
        check, frame = cap.read()
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
        predictions = model.predict(data)

        # confidence threshold is 90%.
        conf_threshold = 90
        confidence = []
        conf_label = ""
        threshold_class = ""

        # for each one of the classes
        for i in range(0, len(classes)):
            # scale prediction confidence to % and apppend to 1-D list
            confidence.append(int(predictions[0][i]*100))

        print(confidence[0])
        # original video feed implementation
        #cv2.imshow("Capturing", data)
        # cv2.waitKey(10)
