from flask import request, url_for
from flask_api import FlaskAPI
import requests
from PIL import Image, ImageDraw, ImageFont
import os, sys, datetime
from io import BytesIO
import base64
import json
import smtplib

app = FlaskAPI(__name__)

def card_repr(key):
    return {'url': request.host_url.rstrip('/') + url_for('show_card', key=key)}

def card_generator(data):
    cardDimension = {'top': (320, 32), 'left': (128, 136), 'right': (192, 136), 'bottom': (320, 32)}

    #get logo
    url = data['logo']
    res = requests.get(url)
    left = Image.open(BytesIO(res.content))
    left.thumbnail((cardDimension['left'][0], cardDimension['left'][0]*left.size[1]/left.size[0]))

    #get Name and Expiry
    name = data['firstName'] + ' ' + data['lastName']
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
    buffer = BytesIO()
    card.save("_".join((data['firstName'], data['lastName'])), format='PNG')
    return base64.b64encode(buffer.getvalue())

def sendCard(card64, receiver):
    from email.message import EmailMessage
    from email.headerregistry import Address
    from email.utils import make_msgid

    # Create the base text message.
    msg = EmailMessage()
    msg['Subject'] = "UTAS HKSA"
    msg['From'] = "devjuniorkm@gmail.com"
    msg['To'] = "moklavie@gmail.com" #receiver

    msg.set_content("Please Enable HTML Views")

    msg.add_alternative("""\
    <html>
      <head></head>
      <body>
        <img src="data:image/png;base64, {}" alt="Red dot" />
      </body>
    </html>
    """.format(card64, subtype='html'))

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], '*XNj7vKM')
    s.send_message(msg)
    s.quit()

#Routes
@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/create/', methods=['GET', 'POST'])
def createCard():
    if request.method == 'POST':
        data = request.data.get('data')
        card64 = card_generator(data)
        sendCard(card64, data['email'])
    return {'status':'403', 'error':'Request Forbidden'}

if __name__ == "__main__":
    app.run(debug=True)
