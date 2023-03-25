from pytube import YouTube
from pytube import Playlist
from pathlib import Path
from _utils import slowPrint, renderProgressBar, handleTimeout, G_DL_PATH
import signal
import os

def downloadSong(url, path):
	if Path.exists(path) == 0:
		os.mkdir(path)
	yt = YouTube(url)
	audio = yt.streams.get_audio_only()
	audio.download(path)

def downloadSingleSong(url, path):
	slowPrint("\nSearching \"{}\"...\n\n".format(url))
	signal.signal(signal.SIGALRM, handleTimeout)
	signal.alarm(30)
	renderProgressBar(0, 1)
	try:
		downloadSong(url, path)
	except Exception as err:
		return print(err)
	renderProgressBar(2, 1)
	slowPrint("\nYour song was downloaded successfully !\n")

def downloadList(urls, length, plTitle):
	count = 1
	timedOutUrls = []
	for url in urls:
		signal.alarm(30)
		renderProgressBar(count, length)
		try:
			downloadSong(url, G_DL_PATH/plTitle)
		except Exception as err:
			timedOutUrls.append(url)
			print(err)
		count += 1
	return timedOutUrls

def downloadSongPlaylist(url):
	slowPrint("\nSearching \"{}\"...\n\n".format(url))
	pl = Playlist(url)
	if pl.length == 0:
		return slowPrint("Playlist looks empty...\n")
	if Path.exists(G_DL_PATH/pl.title) == 0:
		os.mkdir(G_DL_PATH/pl.title)
	signal.signal(signal.SIGALRM, handleTimeout)
	timedOutUrls = downloadList(pl.video_urls, pl.length, pl.title)
	for i in range(2):
		if len(timedOutUrls):
			slowPrint("\n{} song(s) could not be downloaded.\nRetrying now.\n".format(len(timedOutUrls)))
			timedOutUrls = downloadList(timedOutUrls, len(timedOutUrls), pl.title)
	error = len(timedOutUrls)
	renderProgressBar(pl.length + 1, pl.length)
	if error == 0:
		slowPrint("\nYour playlist was downloaded successfully !\n")
	elif error == 1:
		slowPrint("\nYour playlist could not be downloaded entirely... 1 song is missing !\n")
	else:
		slowPrint("\nYour playlist could not be downloaded entirely... {} songs are missing !\n".format(error))


# https://www.youtube.com/watch?v=D52riWqo-ZY

