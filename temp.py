import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("admin.txt", "admin.txt.aes", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("admin.txt.aes", "adminout.txt", password, bufferSize)