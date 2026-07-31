import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture19.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelxy = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=3)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY Edge Detection", sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
