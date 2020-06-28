import cv2

def img_capture(video):
    cap = cv2.VideoCapture(video)
    ret,frame = cap.read()
    num=0
    while ret and num <= 1296:
        if num > 1056 and num % 3 == 0 :
            cv2. imwrite("img%d.png" % num,frame)
            print("已保存第%d帧画面\n" % num)
        ret, frame = cap.read()
        num+= 1
        
    

img_capture("2017编程猫夏令营.mp4")
exit = input("按下回车键，离开源码世界")