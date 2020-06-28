from PIL import Image
import argparse

parser = argparse.ArgumentParser()


parser.add_argument("file")


args = parser.parse_args()

im = args.file
gray=256

ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def get_char(gray,alpha = 256):
	if alpha ==0:
		return " "
	length = len(ascii_char)

	grey = im.getpixel((j,i))
	return ascii_char[int(grey/256*length)]

im = Image.open(im)
im = im.resize((270,270),)
im = im.convert("L") 

txt=""

for i in range(270):
	for j in range(270):
		txt += get_char(gray)
		txt += get_char(gray)
	txt+="\n"	

print("转换成功")

f= open("output.txt","w")
f.write(txt)
f.close()

