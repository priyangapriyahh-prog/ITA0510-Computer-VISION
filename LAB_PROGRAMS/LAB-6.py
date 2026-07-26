import cv2
video = cv2.VideoCapture(r"C:\Users\Priyanga\OneDrive\Desktop\cv\vide0.mp4")
delay = 30
while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
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
video.release()
cv2.destroyAllWindows()
