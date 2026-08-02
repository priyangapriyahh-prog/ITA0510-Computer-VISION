import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture36.jpg")
cv2.imshow("Original Image", img)
cv2.putText(img,"Watch Detected",(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)
cv2.imshow("Recognized Watch", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
