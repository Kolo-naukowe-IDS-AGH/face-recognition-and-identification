import cv2

class Camera:
    def __init__(self, source: int):
        self.capture_device = cv2.VideoCapture(source, cv2.CAP_DSHOW)  # prepare the camera

    def get_frame(self):

        s, img = self.capture_device.read()
        if s:  # frame captured without errors...

            pass

        return img

    def release_camera(self):
        self.capture_device.release()

    def find_faces(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        found_faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)

        #print(found_faces)

        if len(found_faces) != 0: # at least 1 face found
            for (x, y, w, h) in found_faces:
                image = cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)
                
                roi_color = image[y:y + h, x:x + w]
                cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
        else:   # no face found
            return image
        
        return image


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def main():
   while True:
       
        frame = Camera(0).get_frame()
        frame = Camera(0).find_faces(frame)
        cv2.imshow("Frame", frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        Camera(0).release_camera()

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()