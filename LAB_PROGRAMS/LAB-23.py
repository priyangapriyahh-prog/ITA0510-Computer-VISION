import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture23.jpg")
blur = cv2.GaussianBlur(img, (5,5), 0)
sharpen = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Sharpened Image", sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()
