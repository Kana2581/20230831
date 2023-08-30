import cv2
import numpy as np
def getAboveThresholdMean(image,T):
    m1=0
    m2=0
    count=0
    height, width = image.shape[:2]
    for i in range(height):
        for j in range(width):
            if image[i][j]>T:
                m1+=image[i][j]
                count+=1
            else:
                m2+=image[i][j]
    return m1/count,m2/(width*height-count)


def auto(f,t):
    T=cv2.mean(f)[0]
    print(T)
    count=0
  
    while True:
        mean_1,mean_2 =getAboveThresholdMean(f,T)
        if np.abs(0.5*(mean_1+mean_2)-T)<t:
            print(count)
            return 0.5*(mean_1+mean_2)
        else:
            count+=1
            T=0.5*(mean_1+mean_2)




image=cv2.imread('Fig0734(a).tif',cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, int(auto(image,0.5)), 255, cv2.THRESH_BINARY)
cv2.imshow('result',binary_image)
cv2.waitKey(0)
