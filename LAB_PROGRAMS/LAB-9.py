import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture 9.jpg")
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter)
cv2.waitKey(0)
cv2.destroyAllWindows()
