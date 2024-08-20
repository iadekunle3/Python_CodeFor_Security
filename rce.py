import os
import magic
import shutil

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

def validate_file(filepath):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(filepath)
    return file_type in {'image/jpeg', 'image/png', 'image/gif'}

def handle_file_upload(file, upload_dir):
    if not allowed_file(file.filename):
        return "Invalid file type."
    filepath = os.path.join(upload_dir, file.filename)
    file.save(filepath)
    if not validate_file(filepath):
        os.remove(filepath)
        return "Invalid file content."
    os.chmod(filepath, 0o644)
    return "File uploaded successfully."

def main():
    upload_dir = '/path/to/upload/directory'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    # Example file handling
    with open('example.png', 'rb') as file:
        result = handle_file_upload(file, upload_dir)
        print(result)

if __name__ == '__main__':
    main()
