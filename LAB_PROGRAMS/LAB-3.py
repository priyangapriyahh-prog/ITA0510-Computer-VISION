import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture3.jpg")
edges = cv2.Canny(img, 100, 200)
cv2.imshow("Original", img)
cv2.imshow("Canny Outline", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
