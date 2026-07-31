import cv2
img = cv2.imread(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Picture26.jpg")
cv2.imshow("Original Image", img)
watermark = img.copy()
cv2.putText(watermark,
            "PRIYANGA",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2)
cv2.imshow("Watermarked Image", watermark)
cv2.imwrite(r"C:\Users\Priyanga\OneDrive\Desktop\cv\Watermarked_Picture26.jpg", watermark)
cv2.waitKey(0)
cv2.destroyAllWindows()
