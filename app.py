# module 
from cryptography.fernet import Fernet

# class 
class Encryptor:

    # generating a key 
    def generate_key(self):
        key = Fernet.generate_key()
        return key
    
    # writing a key to a file
    def write_key(self, key, key_file):
        with open(key_file, 'wb') as file:
            file.write(key)

    # loading the key from a file
    def load_key(self, key_file):
        with open(key_file, 'rb') as file:
            key = file.read()
        return key

    # encrypting a file 
    def encrypt_file(self, key, original_file, encrypted_file):
        
        # Create a Fernet instance with the encryption key
        f = Fernet(key)

        # Read the contents of original file
        with open(original_file, 'rb') as file:
            original_data = file.read()
        
        # encrypt the original data using Fernet 
        encrypted_data = f.encrypt(original_data)

        # write the encrypted data to encrypted file
        with open(encrypted_file, 'wb') as file:
            file.write(encrypted_data)

    # decrypting a file
    def decrypt_file(self, key, encrypted_file, decrypted_file):
        
        # create a Fernet instance with the encryption key
        f = Fernet(key)

        # read the contents of the encrypted file
        with open(encrypted_file, 'rb') as file:
            encrypted_data = file.read()

        # decrypt the data and store it to encrypted_data, decrypt it using a Fernet
        decrypted_data = f.decrypt(encrypted_data)

        # write the decrypted data to decrypted file
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted_data)
