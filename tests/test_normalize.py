import os
import cv2
import dlib
import numpy as np

from normalize import normalise


def test_for_straight_face():
    path = '../TwarzeDoTestow'
    people = os.listdir(path)
    X = []

    for person in people:
        print(os.path.join(path, person))
        for name in os.listdir(os.path.join(path, person)):
            file_name = name
        img = cv2.imread(os.path.join(path, person, file_name))
        X.append(img)

    X = np.array(X)
    X_normalized = normalise(X)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    for image in X_normalized:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 1)
        for rect in rects:
            shape = predictor(gray, rect)
            shape_np = np.zeros((68, 2), dtype="int")
            for i in range(0, 68):
                shape_np[i] = (shape.part(i).x, shape.part(i).y)
            shape = shape_np

            leftEyePts = shape[36:42]
            rightEyePts = shape[42:48]
            leftEyeCenter = leftEyePts.mean(axis=0).astype("int")
            rightEyeCenter = rightEyePts.mean(axis=0).astype("int")

            dY = rightEyeCenter[1] - leftEyeCenter[1]
            dX = rightEyeCenter[0] - leftEyeCenter[0]
            angle = np.degrees(np.arctan2(dY, dX))

            assert np.abs(angle)<10, "The angle between eyes is {0}".format(angle)
            print(np.abs(angle))


