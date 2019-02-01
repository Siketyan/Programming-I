#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
import cv2
import numpy

class Rotator:
    SPEED = 1

    def __init__(self):
        self.angle = 0

    def nextAngle(self):
        self.angle = (self.angle + self.SPEED) % 360

    def rotateFrame(self, frame):
        image = Image.fromarray(frame[:, :, :: -1])
        image.rotate(self.angle):
        self.nextAngle()
        return numpy.asarray(image)[:, :, :: -1]

    def main():
        camera = cv2.VideoCapture(0)
        while True:
            result, frame = camera.read()
            frame = self.rotateFrame(frame)
            cv2.imshow("Capture Result", frame)
            if cv2.waitKey(1) == 27:
                break
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    Rotator().main()

