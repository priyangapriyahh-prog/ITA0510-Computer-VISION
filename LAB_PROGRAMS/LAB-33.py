import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture33.jpg")
cv2.imshow("Original Image", img)
kernel = np.ones((5,5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Morphological Gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
