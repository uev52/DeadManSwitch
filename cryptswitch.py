import datetime, time
import pyAesCrypt as crypt
import scraper as tweet

gbr = input('LET OP!- gebruik nooit je eigen account -!\nuw Twitter gebruikersnaam: \n')
ww = input('Voer het Wachtwoord van de Twitter account in: \n')
path = "database.csv"
gebruiker = input("Geef hier de gebruikersnaam van de twitteraccount waarmee de encrptie kan worden gestopt: \n")
tijd = input("geef hier de datum op waarop de tweet is gepost die u zoekt:  jjjj - mm - dd:  ")
sleutel = input("Geef de sleutel/bericht op waarmee de encryptiemechanisme kan worden gestopt: \n")
versleutelBestand = input("Geef hier de volledige pad van het bestand die u wilt versleutelen: \n")
timer = int(input("heeft hier de tijd in minuten,waarop u de timer wilt instellen voordat het mechamisme start: \n"))*60
VersleutelWW = input("Geef hier het wachtwoord op waarmee u de bestanden wilt versleutellen: \n")

#de functie zorgt voor de uieindelijke versleuteling als het versleutelen is geactiveerd
def versleutel(versleutelBestand, ww):	#bestandPad= locatie te versleutelen bestand #wachtwoord = de versleuting ww AES
	print("De versleutelmeganisme is geeactiveerd")
	#bit grootte verleuteling
	bufSize = 64 * 1024
	#AES versleuteling van het betand
	crypt.encryptFile(bestandPad, (versleutelBestand + ".aes"), ww, bufSize)
	print("De encryptie is begonnen, het proces kan niet meer teruggedraait worden")

#deze functie zal uiteindeijk bepalen of de encryptie mechanisme zal worden gesart of niet
def checkAvtivatie(versleutelBestand, ww, timer,tijd,sleutel):
	#deze variabel slaat de inhoud van de tweet op de aangegeven tijdstip in de csv betand
	bericht = tweet.main(gbr, ww, gebruiker, path)
	berichten = bericht
	# deze loop controleerd of er een tweet is gevond op de account door te kijken in de csv bestand
	if not berichten: #als er geen bericht is gevonden ...
		timer =timer - 30
		sleep(20) # er word een pauze ingelast van 20 seconde zodat twitter het account niet blockeerd
		if timer == 0: #... en als de timer is afgegaan , start de versleuteling
			versleutel(versleutelBestand, ww)
		else: #zo niet check net zolanf to de timer is gestopt of er een tweet met de key is verstuurd
			print("Er zijn geen tweets gevonden. Heb gedult er moet nog gecheck worden ...")
			checkAvtivatie(versleutelBestand, ww, timer)
	else: # als er wel een tweet is met de key als inhoud stop het verleutelingsprogramma.
		print(berichten[tijd])
		if berichten[tijd] == sleutel:
			print("Het versleutelmeganisme is uitgeschakeld - overgeschakeld op exit mode")
			exit()
		else:
			checkAvtivatie(versleutelBestand, ww, timer, tijd, sleutel)
			print("okey")

def Doel():
	checkAvtivatie(versleutelBestand, ww, timer,tijd,sleutel)

Doel()



