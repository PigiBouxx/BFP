def AsciiArt():
	with open("Ascii.txt","r") as file:
		AsciiArtFile = file.read()
		print(AsciiArtFile)


def author():
	with open("Author.txt","r") as file:
		InfoAuthor = file.read()
		print(InfoAuthor)


