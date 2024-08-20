import html

def encode_output(user_input):
    return html.escape(user_input)

def main():
    user_input = "<script>alert('XSS');</script>"
    safe_output = encode_output(user_input)
    print(f"Encoded output: {safe_output}")

if __name__ == '__main__':
    main()
