import cv2
car = cv2.CascadeClassifier(r"C:\Users\Priyanga\OneDrive\Desktop\cv\cars.xml")
video = cv2.VideoCapture(r"C:\Users\Priyanga\OneDrive\Desktop\cv\video.mp4")
while True:
    ret, frame = video.read()
    if not ret:
        break
    output = frame.copy()
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    cars = car.detectMultiScale(gray, 1.1, 2)
    for (x, y, w, h) in cars:
        cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Original Video", frame)
    cv2.imshow("Vehicle Detection Video", output)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
