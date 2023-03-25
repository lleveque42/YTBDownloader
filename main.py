from _utils import slowPrint, checkDlDir, G_DL_SONG_PATH
from _download import downloadSingleSong, downloadSongPlaylist
from _ask import askUrl, askDownload, G_DL_PLAYLIST, G_DL_SONG

def main():
	try:
		slowPrint("Welcome to YoutubeDownloader\n\n")
		choice = askDownload()
		checkDlDir()
		if (choice == G_DL_SONG):
			try:
				downloadSingleSong(askUrl("song"), G_DL_SONG_PATH)
			except KeyboardInterrupt:
				return slowPrint("\n\nYou interrupted the song downloading.\n")
			except:
				return slowPrint("Looks like the song you entered does not exist.\n")
		elif (choice == G_DL_PLAYLIST):
			try:
				downloadSongPlaylist(askUrl("playlist"))
			except KeyboardInterrupt:
				return slowPrint("\n\nYou interrupted the playlist downloading.\n")
			except:
				return slowPrint("Looks like the playlist you entered does not exist.\n")
	except KeyboardInterrupt as err:
			return slowPrint("\n\nYou interrupted the program.\n")
	except:
		return slowPrint("\n\nAn error has occured !")

main()
