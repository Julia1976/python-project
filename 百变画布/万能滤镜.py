#万能滤镜
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np 

img = Image.open("tower.png")
rgb = np.asarray(img, dtype="int")

r = rgb[:,:,0]
g = rgb[:,:,1]
b = rgb[:,:,2]
a = rgb[:,:,3]

F = np.array([[0,2,0,1,0],
            [0,1,0,0,1],
            [0,2,2,0,0],
            [2,0,0,0,0]])
            
newr = F[0][0] * r + F[0][1] * g + F[0][2] * b + F[0][3] *a + F[0][4]
newg = F[1][0] * r + F[1][1] * g + F[1][2] * b + F[1][3] *a + F[1][4]
newb = F[2][0] * r + F[2][1] * g + F[2][2] * b + F[2][3] *a + F[2][4]
newa = F[3][0] * r + F[3][1] * g + F[3][2] * b + F[3][3] *a + F[3][4]

#获得画布的宽（y），长（x）数据
y,x=r.shape
#根据数据，生成新的图片，色彩模式为rgb+a（透明度）
im = Image.new("RGBA",(x,y))
#循环每个画布的每个像素点，赋予新的RGBA数值
for j in range(0,x):
    for i in range(0,y):
        im.paste(((int(newr[i,j]),int(newg[i,j]),int(newb[i,j]),int(newa[i,j]))),(j,i,j+1,i+1))
#打开图片
im.show("result.png")
