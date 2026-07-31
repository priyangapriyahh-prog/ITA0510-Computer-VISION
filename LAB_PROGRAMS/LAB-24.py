import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture24.jpg")
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
highboost = cv2.filter2D(img, -1, kernel)
cv2.imshow("Original Image", img)
cv2.imshow("High-Boost Sharpened Image", highboost)
cv2.waitKey(0)
cv2.destroyAllWindows()
