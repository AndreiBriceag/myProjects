from cryptography.fernet import Fernet

# generate key
key = Fernet.generate_key()
with open('python/encrypt/filekey.key', 'wb') as filekey:
    filekey.write(key)

# open key
with open('python/encrypt/filekey.key', 'rb') as filekey:
    key = filekey.read()

# using generated key on line 4
fernet = Fernet(key)

# open original file to encrypt
with open('python/encrypt/important.csv', 'rb') as file:
    original = file.read()

# encrypt the file
encrypted = fernet.encrypt(original)

# open the file in write mode and write encrypted data
with open('python/encrypt/important.csv', 'wb') as encryptedFile:
    encryptedFile.write(encrypted)

# COMMENT ALL BELLOW THIS LINE TO ENCRYPT ONLY

# using the key
fernet = Fernet(key)
 
# open the encrypted file
with open('python/encrypt/important.csv', 'rb') as encFile:
    encrypted = encFile.read()
 
# decrypt the file
decrypted = fernet.decrypt(encrypted)
 
# open the file in write mode and write the decrypted data
with open('python/encrypt/important.csv', 'wb') as dec_file:
    dec_file.write(decrypted)