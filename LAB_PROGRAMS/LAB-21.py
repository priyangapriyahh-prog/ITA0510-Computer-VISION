import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture21.jpg")
kernel = np.array([[1, 1, 1],
                   [1,-8, 1],
                   [1, 1, 1]])
laplacian = cv2.filter2D(img, -1, kernel)
cv2.imshow("Original Image", img)
cv2.imshow("Laplacian Mask Output", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
