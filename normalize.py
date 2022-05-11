import cv2
import dlib
import numpy as np


def normalise(X):
    """
    Makes the faces straight.


    Parameters:
        X (numpy.ndarray)

    """
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
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

            eyesCenter = ((leftEyeCenter[0] + rightEyeCenter[0]) // 2,
                          (leftEyeCenter[1] + rightEyeCenter[1]) // 2)

            M = cv2.getRotationMatrix2D(eyesCenter, angle, 1)

            rotated = cv2.warpAffine(image, M, (w, h))

            X_returned.append(rotated)
    return X_returned
