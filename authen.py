import smtplib
import random
import string

def generate_mfa_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_mfa_code(email, code):
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    message = f"Subject: Your MFA Code\n\nYour MFA code is: {code}"
    server.sendmail('your_email@example.com', email, message)
    server.quit()

def verify_mfa_code(input_code, actual_code):
    return input_code == actual_code

def main():
    email = 'user@example.com'
    mfa_code = generate_mfa_code()
    send_mfa_code(email, mfa_code)
    input_code = input("Enter the MFA code sent to your email: ")
    if verify_mfa_code(input_code, mfa_code):
        print("MFA verification successful.")
    else:
        print("Invalid MFA code.")

if __name__ == '__main__':
    main()
