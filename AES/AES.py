from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import os
import base64
import Key # Importing module containing Diffie-Hellman Key Exchange (DHKE) logic

class AES:
    def __init__(self, key):
        # Use the key exchange to generate a shared AES key
        # `firstCommunicationToMakeKey` uses DHKE to securely establish a shared key between two parties
        self.key = key  # Generate 128-bit AES key via Diffie-Hellman

    # Encrypt data
    def encrypt(self, data: str) -> tuple:
        # Step 1: Generate a random Initialization Vector (IV)
        iv = os.urandom(16)  

        # Step 2: Set up AES cipher with the provided key and IV in CBC mode
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))

        # Step 3: Create an encryptor object for the cipher
        encryptor = cipher.encryptor()

        # Step 4: Pad the plaintext to make its length a multiple of AES's block size (16 bytes)
        padder = PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()

        # Step 5: Encrypt the padded data
        encrypted = encryptor.update(padded_data) + encryptor.finalize()

        # Step 6: Return Base64-encoded ciphertext and IV for safe storage or transmission
        return base64.b64encode(encrypted).decode(), base64.b64encode(iv).decode()

    # Decrypt data
    def decrypt(self, encrypted_data: str, iv: str) -> str:
        # Step 1: Recreate the AES cipher using the same key and IV in CBC mode
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(base64.b64decode(iv)))

        # Step 2: Create a decryptor object for the cipher
        decryptor = cipher.decryptor()

        # Step 3: Decode the Base64-encoded ciphertext and decrypt it
        padded_data = decryptor.update(base64.b64decode(encrypted_data)) + decryptor.finalize()

        # Step 4: Remove the padding from the decrypted data to retrieve the original plaintext
        unpadder = PKCS7(algorithms.AES.block_size).unpadder()
        decrypted = unpadder.update(padded_data) + unpadder.finalize()

        # Step 5: Return the plaintext data
        return decrypted.decode()

# Example Usage
key = Key.firstCommunicationToMakeKey()
aes = AES(key)  # Initialize AES encryption/decryption with the shared key

# Encrypt a message
data = "You cant crack this message."  # Raw plaintext data to be encrypted
encrypted_data, iv = aes.encrypt(data)
print("Raw data:", data)  # Display the original plaintext
print("Encrypted Data:", encrypted_data)  # Display the Base64-encoded ciphertext
print("IV:", iv)  # Display the Base64-encoded IV

# Decrypt the message
decrypted_data = aes.decrypt(encrypted_data, iv)
print("Decrypted Data:", decrypted_data)  # Display the original plaintext after decryption