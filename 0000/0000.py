# BY Ubuntu 15.04 
# python 2.7.6 
# spyder
# -*- coding: utf-8 -*-

from PIL import Image,ImageFont,ImageDraw

im = Image.open("icon.jpg")
im = im.resize((200,200),Image.ANTIALIAS)

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("msyhbd.ttc",60)
draw.text((155,-10), "2", fill = (255,0,0), font = font)
im.save("res.jpg")