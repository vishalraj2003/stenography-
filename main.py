from stegano import lsb as vr
import time
from PIL import Image
import keys
from twilio.rest import Client
import string
import random
import os
import cryptocode

while(True):
	try:
		print("-----------Options-----------")
		print("1. Add msg to image.")
		print("2. Reveal Msg from image.")
		print("3. exit.")
		print("-----------------------------")
		a = input("Choice one of the options: ")
		print("-----------------------------")
		if int(a) == 1:
			# Encryption Key
			key = ""
			values = string.ascii_lowercase+string.ascii_uppercase+string.digits
			for i in range(6):
				key += random.choice(values)
			print("-----------------------------")
			print("Encryption key is: ",key)
			print("-----------------------------")

			# taking number
			a = input("Enter 10 digit india's phone # of person you want send encypted msg key: ")
			number  = "+91"+ a
			keys.my_phone_number = number
			if not a.isnumeric():
				raise Exception("Phone number is always Numeric.")
			elif len(a) != 10:
				raise Exception("Phone number must be of 10 digit.")	
			# print(keys.my_phone_number)


			# SMS Service with random otp
			client = Client(keys.account_sid, keys.auth_token)
			message = client.messages.create(body="your otp is "+key,from_=keys.twilio_number, to=keys.my_phone_number)
			print(message.body)

			# Secret message collecting
			textToHide = input("Please enter your secret message: ")
			# cipher = encrypt(key, textToHide)
			cipher = cryptocode.encrypt(textToHide,key)
			print("-----------------------------")
			print("Your Msg got encrypted. and cipher is ",cipher)
			print("-----------------------------")
			
			# ADD FILE HERE
			filename = input("Enter file name with extention: ")
			conditionFilename = filename.split(".")
			location = os.getcwd()
			
			# Force converting into png format if not
			if conditionFilename[1] != "png":
				im1 = Image.open(filename)
				a = filename.split(".")
				filename = a[0]+"2.png"
				im1.save(filename)

			# Hiding text into image
			secret = vr.hide(filename,cipher)
			secret.save(filename)
			print("-----------------------------")
			print("Encrypted image is saved at location {} with name {}".format(location,filename))
			print("-----------------------------")
			
		elif int(a) == 2:
			
			filename = input("Enter file name with extention: ")
			key = input("Please enter Key to decrypt: ")
			# Revealing text from image
			print("-----------decrypting please wait------------")
			time.sleep(5)
			try:
				clear_message = cryptocode.decrypt(vr.reveal(filename), key) 
				print(clear_message)
				print()
				print()
			except IndexError as e:
				print("Provided image don't have any hidden text in it.")
				print()
				print()
			
		elif int(a)==3:
			break
		else:
			print("\nEnter correct Option that is \"1\",\"2\",\"3\"\n")
				
	except ValueError as e:
		print("\nEnter correct Option that is \"1\",\"2\",\"3\"\n")

		
