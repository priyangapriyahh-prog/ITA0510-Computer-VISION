import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture10.jpg")
rows, cols = img.shape[:2]
# Source points
src = np.float32([[50,50], [300,50], [50,250], [300,250]])
# Destination points
dst = np.float32([[20,80], [280,40], [80,300], [320,280]])
# Compute Homography (DLT)
H, status = cv2.findHomography(src, dst)
# Apply Transformation
output = cv2.warpPerspective(img, H, (cols, rows))
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformation", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
