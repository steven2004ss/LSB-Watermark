import cv2
import numpy as np

#Read images
image1 = cv2.imread("imageA.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("imageB.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite("input1.jpg",image1)
cv2.imwrite("input2.jpg",image2)
#Distract LSB & MSB 4bits
image1_a = np.bitwise_and(image1, 0b11110000)
image2_a = np.bitwise_and(image2, 0b00001111)

#Embed watermark
marked_image = np.bitwise_or(image1_a, image2_a)

#Output marked image
cv2.imwrite('output1.jpg',marked_image)

#Distract marked image's MSB 4bits 
marked_image_b = np.bitwise_and(marked_image, 0b11110000)
image1_b = np.bitwise_and(image1, 0b00001111)

#Recover watermark
recover_image = np.bitwise_or(image1_b, marked_image_b)

#Output rocovered image
cv2.imwrite('output2.jpg', recover_image)
