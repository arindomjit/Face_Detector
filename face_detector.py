import cv2

def face_video():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    video = cv2.VideoCapture(0)
    while True:
        ret, image = video.read()
        
        if not ret:
            continue
        image = cv2.flip(image, 1)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)
        #print(faces)
        for(x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 1)
            
        cv2.imshow('Face Detector', image)
        k=cv2.waitKey(10)
        
        if k==ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def face_image():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    image = cv2.imread("0.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray_image,
    scaleFactor=1.05,
    minNeighbors=5)

    while(True):
        for x,y,w,h in faces:
            image=cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0),1)
            cv2.imshow("Face Detector", image)
            #cv2.imwrite("0_rectangle.jpg", image)
            k=cv2.waitKey(0)
            if k==ord('q'):
                break
        break   
    cv2.destroyAllWindows()
        
if __name__ == '__main__':
    face_video()
    face_image()