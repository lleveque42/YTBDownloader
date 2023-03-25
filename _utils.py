from time import sleep
from pathlib import Path
from progress.bar import Bar
import sys
import os

G_TIMESTAMP = 0
G_DL_PATH = Path.home()/'Downloads/YTBDownloads'
G_DL_SONG_PATH = Path.home()/'Downloads/YTBDownloads/Songs'

def renderProgressBar(count, length):
	barTitle = 'Downloading {} of {}...'.format(count, length)
	if count > length:
		barTitle = "Downloads completed !"
	with Bar(barTitle) as bar:
		for i in range(int((count - 1) * 100 / length)):
			bar.next()

def slowPrint(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		sleep(G_TIMESTAMP)

def slowInput(str):
	slowPrint(str)
	return input(" : ")

def checkDlDir():
	if Path.exists(G_DL_PATH) == 0:
		os.mkdir(G_DL_PATH)
	if Path.exists(G_DL_SONG_PATH) == 0:
		os.mkdir(G_DL_SONG_PATH)
	return G_DL_PATH

def handleTimeout(signum, frame):
	raise TimeoutError("\nTimeoutError: An error occured and a song could not be downloaded...\n")

