import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture40.jpg")
cv2.imshow("Original Image", img)
output = img.copy()
cv2.rectangle(output, (100, 100), (300, 300), (0, 255, 0), 2)
object_img = img[100:300, 100:300]
cv2.imshow("Rectangle Image", output)
cv2.imshow("Extracted Object", object_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
