# Criptazione semplice
# Fernet
#
# Libreria

from cryptography.fernet import Fernet 
#
testo = open("chiaro.txt", "r")
testo_da_cifrare = testo.read()
testo_da_cifrare_byte = testo_da_cifrare.encode("utf-8") # da string in bytes array
                                                         # il metodo per criptare accetta
                                                         # una sequenza di byte
#7
chiave = open("chiave.txt","r")

#

chiave_valore = Fernet(chiave.read()) 
# Cifratura
token = chiave_valore.encrypt(testo_da_cifrare_byte) # Fernet Token (testo cifrato)
# It encrypts data passed as a parameter to the method.
# The outcome of this encryption is known as a “Fernet token” which is basically the ciphertext.
# The encrypted token also contains the current timestamp when it was generated in plaintext.
# The encrypt method throws an exception if the data is not in bytes.
# Is a URL-safe base64-encoded
#
# Display
print ('CRIPTAZIONE')
print ()
print ("Chiave: ", chiave)       # debug
print()
print ("Testo in chiaro: ")
print (testo_da_cifrare)
print()
print ("Testo in byte: ")
print (testo_da_cifrare_byte)
print ()
print ("Testo cifrato (token): ")
print (token)
print ("-----------------------------------------------------------")
#
# Decifratura
with open("chiave.txt", "rb") as chiave_file:
    chiave = chiave_file.read()
#
chiave_valore = Fernet(chiave) 
testo_decifrato_byte = chiave_valore.decrypt(token)
testo_decifrato = testo_decifrato_byte.decode("utf-8") # da bytes array a string
#
# Display
print ('DECRIPTAZIONE')
print ()
print ("Chiave: ", chiave)       # debug
print ()
print ("Testo decifrato in byte: ")
print (testo_decifrato_byte)
print ()
print ("Testo decifrato: ")
print (testo_decifrato) 
#
# Ottobre 2022 v. 3.0
#