# Program to resize a image.

# Author:- Mani Agarwal
# Email:- maniagarwal@jklu.edu.in

import cv2

img=cv2.imread("Taylor1.jpg",1)   # 1 is for coloured image.

img_1=cv2.imread("Taylor1.jpg",0) # 0 is for converting the image into gray.

resized_image=cv2.resize(img,(400,400))  # For resizing the image
cv2.imshow("Taylor Swift",resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Note :- You must write waitKey() and destroyAllWindows(), otherwise the error of "Not Responding may come".
