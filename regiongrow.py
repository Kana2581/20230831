# import cv2
# import numpy as np

# def regionGrow(image,S,T):
#     equal_pixels = np.where(image == S, 1, 0)
#     new_image = np.zeros_like(image)
#     new_image[equal_pixels == 1] = 1

    
#     S = np.where(np.abs(image-S)<T, 1, 0)
#     result=cv2.copyTo(new_image,None)
#     result[S==1]=255
#     cv2.imshow('nmsl1',new_image)
#     cv2.imshow('nmsl',result)
#     kernel = np.array([[1, 1, 1],
#                    [1, 1, 1],
#                    [1, 1, 1]], dtype=np.uint8)
#     processed_image = cv2.dilate(result, kernel, iterations=1)
#     cv2.imshow('nmsl',result)
#     cv2.waitKey(0)
# image=cv2.imread('Fig0621(a)(weld-original).tif',cv2.IMREAD_GRAYSCALE)
# float_image = image.astype(np.float32) / 255.0
# regionGrow(float_image,1,0.26)
import cv2
import numpy as np
def arrayAnd(arr1,arr2):
    arr3=np.zeros_like(arr1).astype(np.double)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if bool(arr1[i][j]==1) and bool(arr2[i][j]==1):
                arr3[i][j]=1
            else:
                arr3[i][j]=0
                
    
    return arr3
    
def regionGrow(image,S,T):
    equal_pixels = np.where(image == S, 1, 0)
    new_image = np.zeros_like(image)
    new_image[equal_pixels == 1] = 1

    
    S = np.where(np.abs(image-S)<T, 1, 0)
    result=cv2.copyTo(new_image,None)
    result[S==1]=1
    cv2.imshow('nmsl1',new_image)
    cv2.imshow('nmsl',result)
    kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)
    processed_image = np.zeros_like(image)  
    i=int(0)
    while(True):
        new_image=cv2.dilate(new_image, kernel, iterations=1)
        
        

        new_image=arrayAnd(result,new_image)
        if(np.array_equal(processed_image,new_image)):
            break
        processed_image=new_image


    cv2.imshow('nmsl3',processed_image)
    cv2.waitKey(0)
image=cv2.imread('Fig0621(a)(weld-original).tif',cv2.IMREAD_GRAYSCALE)
float_image = image.astype(np.float32) / 255.0
regionGrow(float_image,1,0.26)


