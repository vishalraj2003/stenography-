# Stenography-
I have made a project on stenograpy as a part of my B.tech Subject named as image processing.

Note: This backend logic for performing Stenograpy on an image. 

**Defination:**

"Digital Watermarking To Hide Text Messages

* User will enter text message.
* System will hide the text message in image uploaded by user.
* System will apply encrypting loop to encrypt the text message in image.
* To decrypt, System will apply decrypting loop to decrypt message from image
* Finally, system will display the text message encrypted within the image"

## Extra Features of the Project.

1. Before writing msg inside image, I have encrypted it. 
2. KEY of the encryption have been shared  using Twilio SMS service.
3. Converts image with format like jpg or png but saves it in the form of png only.

![image](https://user-images.githubusercontent.com/78425418/219710646-8ca4e919-518d-4881-b0f6-6ab8b05a1a6d.png)

Description:
As we can see first we are asking for work to perform like "encrypt msg in image" or "Decrypt msg from image". then key is generated and displayed.

After that we collected phone number to send KEY to that number.

Kindly command this code if send sms is giving error or try to update values in keys.py file.

```
# SMS Service with random otp
			client = Client(keys.account_sid, keys.auth_token)
			message = client.messages.create(body="your otp is "+key,from_=keys.twilio_number, to=keys.my_phone_number)
			print(message.body)
```

After that add msg to encrypt inside image. At last, File name of image have been mentioned.

Location at which image is stored is desplayed so that user can goto that location and fatch the image from there.

![image](https://user-images.githubusercontent.com/78425418/219714192-40022078-87f5-45d8-9796-e757fbb8e5f1.png)
First enter image which has text hidden inside it.
then enter key which you have received on sms.
finally, Hidden text is displayed.

![image](https://user-images.githubusercontent.com/78425418/219715011-52333e47-af21-4e85-8c85-3ec7cabd0c1e.png)

select "3" to exit.

original image:

<img src="https://user-images.githubusercontent.com/78425418/219715391-3297a160-b9cc-4860-8d4c-7128514885e5.png" width="150" height="280">

Image with hidden text:

<img src="https://user-images.githubusercontent.com/78425418/219715680-d76fb001-a241-47e4-8811-7232301042cf.png" width="150" height="280">

