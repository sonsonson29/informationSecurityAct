from app import Encryptor

# create an instance of the class
encryptor=Encryptor()

# create a key 
mykey=encryptor.generate_key()

# write key to a file
encryptor.write_key(mykey, 'mykey.key')

# loade key
loaded_key=encryptor.load_key('mykey.key')

# encrypting a file

encryptor.encrypt_file(loaded_key, 'sample.txt', 'sample_encrypted.txt')
encryptor.decrypt_file(loaded_key, 'sample_encrypted.txt', "sample_decryptedFile.txt")
