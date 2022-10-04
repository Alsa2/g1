# import required module
from cryptography.fernet import Fernet

fernet = Fernet("2wFYfwlLpg4iy_k-wkGxNUH3pGLYdzjFbEyf4jQJfiY=")
 
# opening the original file to encrypt
with open('transactions.csv', 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
 
# opening the file in write mode and
# writing the encrypted data
with open('transactions.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)