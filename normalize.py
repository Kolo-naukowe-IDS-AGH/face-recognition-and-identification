import cv2
import dlib
import numpy as np
import os

def create_array(path):
    people = os.listdir(path)
    X = []

    for person in people:
        for name in os.listdir(os.path.join(path, person)):
            file_name = name
        img = cv2.imread(os.path.join(path, person, file_name))
        X.append(img)

    X = np.array(X)
    return X


def normalize(X):
    """
    Makes the faces straight.


    Parameters:
        X (numpy.ndarray)

    """
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    if(X.ndim==4):
        X_returned = []

        for image in X:

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

                (h, w) = image.shape[:2]

                eyesCenter = (int((leftEyeCenter[0] + rightEyeCenter[0]) // 2),
                              int((leftEyeCenter[1] + rightEyeCenter[1]) // 2))

                M = cv2.getRotationMatrix2D(eyesCenter, angle, 1)

                rotated = cv2.warpAffine(image, M, (w, h))

                X_returned.append(rotated)
        return X_returned

    if(X.ndim==3):
        gray = cv2.cvtColor(X, cv2.COLOR_BGR2GRAY)
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

            (h, w) = X.shape[:2]

            eyesCenter = (int((leftEyeCenter[0] + rightEyeCenter[0]) // 2),
                          int((leftEyeCenter[1] + rightEyeCenter[1]) // 2))

            M = cv2.getRotationMatrix2D(eyesCenter, angle, 1)

            rotated = cv2.warpAffine(X, M, (w, h))
    return rotated