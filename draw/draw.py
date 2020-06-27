from PIL import Image
import argparse


parser = argparse.ArgumentParser()


parser.add_argument('file')

args=parser.parse_args()

im=args.file





im=Image.open(im)

im=im.resize((270,270))

im=im.convert('L')

im.save('result.png')

print('转换成功')