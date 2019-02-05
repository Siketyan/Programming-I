#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv2

class Rectangle:
    def __init__(self, array):
        self.left = array[0]
        self.top = array[1]
        self.width = array[2]
        self.height = array[3]

    def getRight(self):
        return self.left + self.width

    def getBottom(self):
        return self.top + self.height

    def getStartPoint(self):
        return (self.left, self.top)

    def getEndPoint(self):
        return (self.getRight(), self.getBottom())

    def drawOnCv2Image(self, image, color, thickness):
        return cv2.rectangle(
            image,
            self.getStartPoint(),
            self.getEndPoint(),
            color,
            thickness
        )

class Classifier:
    def __init__(self, path):
        self.classifier = cv2.CascadeClassifier(path)
        self.options()

    def options(self, scaleFactor = 1.1, minNeighbors = 1, minSize = (10, 10)):
        self.scaleFactor = scaleFactor
        self.minNeighbors = minNeighbors
        self.minSize = minSize

    def detect(self, image):
        objects = self.classifier.detectMultiScale(
            image,
            scaleFactor = self.scaleFactor,
            minNeighbors = self.minNeighbors,
            minSize = (self.minSize)
        )
        for obj in objects:
            yield Rectangle(obj)

class App:
    WINDOW_TITLE = "Face Detection"
    CASCADE_DIR = "C:\\opencv\\build\\etc\\haarcascades\\" # MUST be ended with \\ or /
    CASCADE_FILE = "haarcascade_frontalface_alt.xml" # requires extension
    CLASSIFIER_SCALE_FACTOR = 1.1
    CLASSIFIER_MIN_NEIGHBORS = 1
    CLASSIFIER_MIN_SIZE = (10, 10) # MUST be tuple value
    RECTANGLE_COLOR = (0x00, 0xFF, 0x00) # MUST be supported on OpenCV
    RECTANGLE_THICKNESS = 2 # px
    ESCAPE_KEY_CODE = 27
    ESCAPE_KEY_TIMEOUT = 1 # ms

    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.classifier = Classifier(self.CASCADE_DIR + self.CASCADE_FILE)
        self.classifier.options(
            self.CLASSIFIER_SCALE_FACTOR,
            self.CLASSIFIER_MIN_NEIGHBORS,
            self.CLASSIFIER_MIN_SIZE
        )

    def drawRectangles(self, frame, rectangles):
        for rectangle in rectangles:
            rectangle.drawOnCv2Image(
                frame,
                self.RECTANGLE_COLOR,
                self.RECTANGLE_THICKNESS
            )

    def detectOnFrame(self, frame):
        grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rectangles = self.classifier.detect(grayscaled)
        self.drawRectangles(frame, rectangles)
        return frame

    def waitEscapeKey(self):
        return cv2.waitKey(self.ESCAPE_KEY_TIMEOUT) == self.ESCAPE_KEY_CODE

    def dispose(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def main(self):
        while True:
            result, frame = self.camera.read()
            frame = self.detectOnFrame(frame)
            cv2.imshow(self.WINDOW_TITLE, frame)
            if self.waitEscapeKey():
                break

if __name__ == "__main__":
    App().main()