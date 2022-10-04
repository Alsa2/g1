from cryptography.fernet import Fernet

fernet = Fernet("2wFYfwlLpg4iy_k-wkGxNUH3pGLYdzjFbEyf4jQJfiY=")

# opening the encrypted file
with open('transactions.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('transactions.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
