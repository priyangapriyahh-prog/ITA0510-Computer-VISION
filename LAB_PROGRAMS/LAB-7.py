import cv2
cap = cv2.VideoCapture(0)
delay = 30
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Web Camera", frame)
    key = cv2.waitKey(delay) & 0xFF
    if key == ord('s') or key == ord('S'):
        delay = 100
        print("Slow Motion")
    elif key == ord('f') or key == ord('F'):
        delay = 5
        print("Fast Motion")
    elif key == ord('q') or key == ord('Q'):
        print("Exit")
        break
cap.release()
cv2.destroyAllWindows()
