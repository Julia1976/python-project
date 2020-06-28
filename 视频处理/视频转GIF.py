import cv2

def img_capture(video):
    cap = cv2.VideoCapture(video)
    ret,frame = cap.read()
    num=0
    while ret:
        cv2. imwrite("img%d.png" %num,frame)
        ret, frame = cap.read()
        num+= 1
        
    

img_capture("编程猫片头.mp4")
exit = input("按下回车键，离开源码世界")