import os
import time

while True:
	print("What can I do for You Ganesh ??")
	p = input()

	if("run" in p) or ("launch" in p) or ("execute" in p) or ("start" in p ):
		if("chrome" in p) or ("browser" in p) or ("google" in p) or ("search engine" in p):
			print("Chrome is Opening....")
			os.system("chrome")
		elif("music" in p) or ("song" in p) or ("media" in p) or ("player" in p):
			print("Media Player is Opening....")
			os.system("wmplayer")
		elif("notepad" in p) or ("texteditor" in p):
			print("notepad is Opening....")
			os.system("notepad")
		elif("paint" in p) or ("mspaint" in p):
			print("mspaint is Opening....")
			os.system("mspaint")
		
		time.sleep(1)
		print()

	elif("quit" in p) or ("exit" in p) or ("close" in p):
		print("Ok Bye...")
		break
	else:
		print("Sorry! I can't get what you want!!")
		print()
	