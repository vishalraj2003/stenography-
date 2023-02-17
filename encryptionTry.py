from simplecrypt import encrypt, decrypt
plaintext = "vishal is cool"
ciphertext = encrypt('password', plaintext)
plaintext2 = decrypt('password', ciphertext)
print(plaintext2)
