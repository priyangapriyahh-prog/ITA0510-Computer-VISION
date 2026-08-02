import cv2
face_cascade = cv2.CascadeClassifier(r"C:\Users\Priyanga\OneDrive\Desktop\cv\haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture38.jpg")
cv2.imshow("Original Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
