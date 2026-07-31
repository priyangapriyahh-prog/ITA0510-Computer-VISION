import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture16.jpg")
rows, cols = img.shape[:2]
src = np.float32([[50,50], [300,50], [50,250], [300,250]])
dst = np.float32([[20,80], [280,40], [80,300], [320,280]])
H, status = cv2.findHomography(src, dst)
output = cv2.warpPerspective(img, H, (cols, rows))
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformation", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
