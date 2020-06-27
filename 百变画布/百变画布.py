#百变画布
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

img = Image.open("tower.png")
rgb=np.asarray(img, dtype = 'int')

newr = rgb[:,:,0]
newg = rgb[:,:,1]
newb = rgb[:,:,2]
newa = rgb[:,:,3]

newr[:] = 255
newg[:] = 255
newb[:] = 255
newa[:] = 255

#获得画布宽（y）/长（x）数据
y,x=newr.shape
#根据数据，生成新的图片，色彩模式为RGB+A（透明度）
im = Image.new("RGBA",(x,y))
#循环为画布的每个像素点，赋予新的RGBA数值
for j in range(0,x):
    for i in range(0,y):
        im.paste(((int(newr[i,j]),int(newg[i,j]),int(newb[i,j]),int(newa[i,j]))),(j,i,j+1,i+1))
        
#输出结果，保存为png格式图片
im.save("result_red.png")
