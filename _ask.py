from _utils import slowPrint, slowInput

G_DL_SONG = "1"
G_DL_PLAYLIST = "2"

def askDownload():
	choice = slowInput("What do you want to download ?\n1) Single song\n2) Whole playlist\n\nYour choice")
	if choice == G_DL_SONG or choice == G_DL_PLAYLIST:
		rep = "a single song" if choice == G_DL_SONG else "a whole playlist"
		slowPrint("You chose to download {}.\n".format(rep))
		return choice
	else:
		slowPrint("\nYour choice must be included between 1 or 2.\nPlease re-enter.\n\n")
		return askDownload()

def askUrl(choice):
	return slowInput("\nPlease enter the url of the {} you want to download".format(choice))

