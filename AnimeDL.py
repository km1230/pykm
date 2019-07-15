import urllib.request
import os
import threading
import time
import re

"""
checkWholeSeries when file name is not a string
1. True for downloading whole series
2. False for downloading a single episode
"""
def checkWholeSeries():
	if re.match(r'[yY]', wholeSeries, re.I):
		return True
	else:
		return False

"""
createFolder
1. Create folder with anime name
2. change currect working directory to destination
"""
def createFolder():
	os.chdir(directory)
	if not os.path.exists(animeName):
		os.mkdir(animeName)
	os.chdir(animeName)

"""
Download
1. Create Folder
2. try - download numeric file name
3. except - download string file name as defined
"""
def download():
	createFolder()
	print('Start downloading to: ' + os.getcwd())
	try:
		e = int(episodes)
		if checkWholeSeries():
			for i in range(1, e+1):
				file = animeUrl + str(i) + '.mp4'
				urllib.request.urlretrieve(file, str(i) + '.mp4')
		else:
			file = animeUrl + str(e) + '.mp4'
			urllib.request.urlretrieve(file, str(e) + '.mp4')
	except ValueError:
		file = animeUrl + episodes + '.mp4'
		urllib.request.urlretrieve(file, episodes +'.mp4')
	print('Done.')

"""
Loading
1. Show animation when downloading
"""
def loading():
	animation = '|/-\\'
	for a in animation:
		print('...' + a, end='\r')
		time.sleep(0.1)

"""
Custom detail
1. Name of anime as folder name
2. URL of the anime folder on the website
3. Is the file an OVA or a series of episodes
4. Get Local Directory location
"""
animeName = input('Anime Name: ') #Will be folder name
animeUrl = input('Valid Link of Parent Folder: ') #e.g. https://rem.anime1.app/494/
while True:
	special = input('Original file name is string?(y/n) ')
	if re.match(r'[yY]', special, re.I):
		print('**This will only download a single file**')
		episodes = input('File name?(excludes format) ')
		break
	elif re.match(r'[nN]', special, re.I):
		wholeSeries = 'x'
		while re.match(r'[^nNyY]', wholeSeries, re.I):
			wholeSeries = input('Download the whole series in order?(y/n) ')
		if checkWholeSeries():
			episodes = int(input('Number of episodes: '))
		else:
			episodes = int(input('Which episode? '))
		break
	else:
		print('Please enter y/n')

directory = os.path.expanduser('~/Desktop/Anime/')

"""
Run the Program
"""
process = threading.Thread(target=download)
process.start()
while process.isAlive():
	loading()