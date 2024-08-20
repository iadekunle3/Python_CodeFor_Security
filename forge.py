import secrets

def generate_csrf_token():
    return secrets.token_hex(32)

def validate_csrf_token(session_token, form_token):
    return session_token == form_token

def main():
    session_token = generate_csrf_token()
    form_token = input("Enter the CSRF token from the form: ")
    if validate_csrf_token(session_token, form_token):
        print("CSRF token validation successful.")
    else:
        print("Invalid CSRF token.")

if __name__ == '__main__':
    main()
