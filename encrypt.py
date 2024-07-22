from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Sensitive data example (e.g., patient's health metric)
sensitive_data = b"Patient heart rate: 75 BPM"

# Encrypt the data
encrypted_data = cipher_suite.encrypt(sensitive_data)
print(f"Encrypted data: {encrypted_data}")

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)
print(f"Decrypted data: {decrypted_data.decode()}")
