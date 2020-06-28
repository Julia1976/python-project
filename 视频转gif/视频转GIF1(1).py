import cv2
import imageio

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
        
def gif_save():
    print("gif合成中，请稍后......\n")
    images=[]
    for num in range(1059,1297,3):
        img=imageio.imread("img%d.png" % num)
        images.append(img)
    imageio.mimsave("编程猫.gif", images , fps=8)
    print("gif保存成功！\n")


img_capture("2017编程猫夏令营.mp4")
gif_save()

exit = input("按下回车键，离开源码世界")