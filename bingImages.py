import requests
from bs4 import BeautifulSoup as bs
from io import BytesIO as bio
from PIL import Image

search = ('+').join(input('Looking for: ').split())
searchEngine = 'https://www.bing.com/images/search?q=' + search + '&FORM=HDRSC2'
r = requests.get(searchEngine)
print('Reaching server...')
if r.status_code == 200:
	print('Reached server. Listening...')
	code = bs(r.text,'html.parser')
	link = code.find('a', class_='thumb').get('href')
	imgLink = requests.get(link)
	if imgLink.status_code == 200:
		print('Item found...')
		img = Image.open(bio(imgLink.content))
		print('Downloading...')
		img.save(link[-15:-5] + '.' + img.format)
		print('Image saved!')