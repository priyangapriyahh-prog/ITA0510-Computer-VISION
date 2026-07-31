import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture27.jpg")
cv2.imshow("Original Image", img)
crop = img[50:150, 50:150]
img[200:300, 200:300] = crop
cv2.imshow("Cropped, Copied and Pasted Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
