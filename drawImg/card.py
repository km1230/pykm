from PIL import Image, ImageDraw, ImageFont
import os, sys, datetime

cardDimension = {'top': (320, 32), 'left': (128, 136), 'right': (192, 136), 'bottom': (320, 32)}

#get logo
file = './logo.jpg'
left = Image.open(file)
left.thumbnail((cardDimension['left'][0], cardDimension['left'][0]*left.size[1]/left.size[0]))

#get Name and Expiry
name = 'Hello World'
expiry = datetime.datetime.fromtimestamp(1580389200000/1000.0).strftime('%Y %b')

#create parts
top = Image.new('RGB', cardDimension['top'], color='#ffc107')
right = Image.new('RGB', cardDimension['right'], color='#ffffff')
bottom = top = Image.new('RGB', cardDimension['bottom'], color='#ffc107')

#find top and bottom for left part to paste on
leftTop = round((cardDimension['left'][1] - left.size[1]) * 0.5) + cardDimension['top'][1]
leftBottom = leftTop + left.size[1]


#pasting Images to card
#card.paste(left, top, right, bottom)
card = Image.new('RGB', (320, 200), color='#FFFFFF')
card.paste(top, (0, 0, cardDimension['top'][0], cardDimension['top'][1]))
card.paste(right, (left.size[0], cardDimension['top'][1], 320, cardDimension['top'][1] + cardDimension['right'][1]))
card.paste(bottom, (0, cardDimension['top'][1] + cardDimension['right'][1], 320, 200))
card.paste(left, (0, leftTop, left.size[0], leftBottom))

#Write text on card
draw = ImageDraw.Draw(card)
bigfnt = ImageFont.truetype('./sriracha.ttf', 20)
smallfnt = ImageFont.truetype('./sriracha.ttf', 12)

draw.text((cardDimension['left'][0]+15, cardDimension['top'][1]+20), 'Name: ', '#000000', font=smallfnt)
draw.text((cardDimension['left'][0]+20, cardDimension['top'][1]+42), name, '#000000', font=smallfnt)
draw.text((cardDimension['left'][0]+15, cardDimension['top'][1]+74), 'Expiry:', '#000000', font=smallfnt)
draw.text((cardDimension['left'][0]+20, cardDimension['top'][1]+96), expiry, '#000000', font=smallfnt)
draw.text((110, 0), 'UTAS HKSA', '#000000', font=bigfnt)
draw.text((90, 165), 'Membership Card', '#000000', font=bigfnt)

#img.save(filename)
card.save('card.jpg')
