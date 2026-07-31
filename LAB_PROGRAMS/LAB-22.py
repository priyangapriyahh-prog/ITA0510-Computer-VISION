import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture22.jpg")
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpen = cv2.filter2D(img, -1, kernel)
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()
