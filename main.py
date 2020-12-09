import cv2
import numpy as np
left=cv2.imread("left.png")
right=cv2.imread("right.png")
left=cv2.cvtColor(left,cv2.COLOR_BGR2GRAY)
right=cv2.cvtColor(right,cv2.COLOR_BGR2GRAY)


spacing=40
look=2

lookL=2*look+1
xsize=left.shape[1]-(2*look+spacing)
ysize=left.shape[0]-2*look
result=np.zeros((ysize,xsize,1),"uint8")

for x in range(xsize):
    print(x)
    for y in range(ysize):
        bestTotal=255*lookL*lookL
        value=0
        for s in range(spacing):
            difference=cv2.absdiff(left[y:y+lookL,x+s:x+lookL+s],right[y:y+lookL,x:x+lookL])

            total=0
            for cachex in range(lookL):
                for cachey in range(lookL):
                    total+=difference[cachey,cachex]
            if total<bestTotal:
                bestTotal=total
                value=s*6
        result[y,x]=value

cv2.imwrite("result.png",result)
cv2.imshow('original', result)
cv2.waitKey(0)
cv2.destroyAllWindows()