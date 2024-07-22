import hashlib

# Sample user credentials
users = {
    "doctor": hashlib.sha256(b"doctor_password").hexdigest(),
    "nurse": hashlib.sha256(b"nurse_password").hexdigest()
}

def authenticate(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == password_hash:
        return True
    return False

# Example usage
username = "doctor"
password = "doctor_password"

if authenticate(username, password):
    print("Authentication successful")
else:
    print("Authentication failed")
