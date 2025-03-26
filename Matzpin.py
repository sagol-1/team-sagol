from AES import AES, Key
from CHECKSUM import Checksum
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import base64

# Generate RSA key pair
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt data using RSA and AES
def encrypt(data, public_key):
    # Step 1: Generate AES key
    aes_key = Key.firstCommunicationToMakeKey()
    aes = AES.AES(aes_key)

    # Step 2: Encrypt the data using AES
    encrypted_data = aes.encrypt(data)

    # Step 3: Encrypt the AES key using RSA
    rsa_key = RSA.import_key(public_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    # Step 4: Combine the encrypted AES key and encrypted data
    combined_data = base64.b64encode(encrypted_aes_key).decode() + ":" + encrypted_data

    # Step 5: Add checksum for validation
    secured_data = Checksum.createChecksum(combined_data)

    return secured_data

# Decrypt data using RSA and AES
def decrypt(secured_data, private_key):
    # Step 1: Validate checksum
    result, combined_data = Checksum.checkChecksumValidation(secured_data)
    if not result:
        raise ValueError("Checksum validation failed!")

    # Step 2: Split the encrypted AES key and encrypted data
    encrypted_aes_key, encrypted_data = combined_data.split(":")

    # Step 3: Decrypt the AES key using RSA
    rsa_key = RSA.import_key(private_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    aes_key = rsa_cipher.decrypt(base64.b64decode(encrypted_aes_key))

    # Step 4: Decrypt the data using AES
    aes = AES.AES(aes_key)
    decrypted_data = aes.decrypt(encrypted_data)

    return decrypted_data

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()

    # Save keys to files (optional)
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)

    # Encrypt a message
    message = "This is a secret message."
    print("Original message:", message)
    encrypted_message = encrypt(message, public_key)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)