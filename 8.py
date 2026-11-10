pip install cryptography 7. Implement data encryption and data decryption
Procedure:
1. Make a secret key & IV (random numbers).
2. Take a message (plaintext).
3. Add padding so message fits AES block size (16 bytes).
4. Encrypt → message turns into secret code (ciphertext).
5. Decrypt → secret code turns back to the original message.
Program:
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
# Function to generate a random key and initialization vector 
def generate_key_and_iv():
 key = os.urandom(16) 
 iv = os.urandom(16) 
 return key, iv
def encrypt(plaintext, key, iv):
 # Pad plaintext to ensure it's a multiple of block size (16 bytes)
 padder = padding.PKCS7(128).padder() # AES block size is 128 bits
 padded_data = padder.update(plaintext.encode()) + padder.finalize()
 # Create AES cipher and encrypt data
 cipher = Cipher(algorithms.AES(key), modes.CBC(iv), 
backend=default_backend())
 encryptor = cipher.encryptor()
 ciphertext = encryptor.update(padded_data) + encryptor.finalize()
 return ciphertext
# Function to decrypt ciphertext
def decrypt(ciphertext, key, iv):
 # Create AES cipher and decrypt data
 cipher = Cipher(algorithms.AES(key), modes.CBC(iv), 
backend=default_backend())
 decryptor = cipher.decryptor()
 padded_data = decryptor.update(ciphertext) + decryptor.finalize()
# Unpad the decrypted data
 unpadder = padding.PKCS7(128).unpadder()
 plaintext = unpadder.update(padded_data) + unpadder.finalize()
 return plaintext.decode()
# Main function to demonstrate encryption and decryption
def main():
 print("AES Encryption and Decryption")
 
 # Generate key and IV
 key, iv = generate_key_and_iv()
 print(f"Generated Key: {key.hex()}")
 print(f"Generated IV: {iv.hex()}")
 # Input plaintext
 plaintext = input("\nEnter plaintext to encrypt: ")
 # Encrypt plaintext
 ciphertext = encrypt(plaintext, key, iv)
 print(f"\nCiphertext (hex): {ciphertext.hex()}")
 # Decrypt ciphertext
 decrypted_text = decrypt(ciphertext, key, iv)
 print(f"\nDecrypted text: {decrypted_text}")
if __name__ == "__main__":
 main()
OUTPUT:
AES Encryption and Decryption
Generated Key: a2ca8510bc5dc514a933ecf823e38743
Generated IV: a4ed453273fdfa4f9d0cc9e59a1a19cf
Enter plaintext to encrypt: hello world
Ciphertext (hex): f2eb13b3b54ded7226c5ffc1fadbf5f2
Decrypted text: hello world
