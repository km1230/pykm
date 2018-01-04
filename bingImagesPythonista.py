#Pythonista Version
import requests
from io import BytesIO as bio
from PIL import Image
from bs4 import BeautifulSoup as bs
import photos

search = input('Search for: ').replace(' ', '+')
page = 'http://www.bing.com/images/search?q='+search+'&FORM=HDRSC2'
r = requests.get(page)

def GetContent(r):
	content = bs(r.text, 'html.parser')
	results = content.find('div', class_='cico')
	src = results.img['src'].split('&w=')[0]
	print(src)
	return src

def SavePic(src):
	try:
		pic = Image.open(bio(requests.get(src).content))
		photos.save_image(pic)
		print('Image saved.')
	except:
		print('Failed to save image.')

print('Loading...')
if r.status_code == 200:
	print('Reached Server. Searching...')
	src = GetContent(r)
	SavePic(src)	
else:
	print('Server Error.')
	
