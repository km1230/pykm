import urllib.request
import os
import threading
import time

#Custom detail
animeName = input('Anime Name: ') #Will be folder name
animeUrl = input('Valid Link of Parent Folder: ') #e.g. https://rem.anime1.app/494/
episodes = int(input('Number of episodes: '))

#Destination: Desktop + Anime Name
desktop = os.path.expanduser('~/Desktop')

def createFolder():
	os.chdir(desktop)
	if not os.path.exists(animeName):
		os.mkdir(animeName)
	os.chdir(animeName)

def download():
	createFolder()
	print('Start downloading to: ' + os.getcwd())
	for i in range(1, episodes+1):
		file = animeUrl + str(i) + '.mp4'
		urllib.request.urlretrieve(file, str(i)+'.mp4')
	print('Done.')

def loading():
	animation = '|/-\\'
	for a in animation:
		print('...' + a, end='\r')
		time.sleep(0.1)

process = threading.Thread(target=download)
process.start()
while process.isAlive():
	loading()
process.stop()