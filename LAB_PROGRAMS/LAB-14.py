import cv2
import numpy as np
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture 9.jpg")
rows, cols = img.shape[:2]
pts1 = np.float32([[50,50], [300,50], [50,250], [300,250]])
pts2 = np.float32([[10,100], [300,50], [100,300], [280,280]])
H, status = cv2.findHomography(pts1, pts2)
output = cv2.warpPerspective(img, H, (cols, rows))
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
