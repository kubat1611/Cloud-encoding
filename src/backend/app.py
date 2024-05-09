from flask import Flask, request, jsonify
from src.backend.controllers import generate_key, encrypt_file, decrypt_file, upload_to_drive, download_from_drive, get_files_info_from_drive
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to the CloudEncoding API!'


@app.route('/encrypt-upload', methods=['POST'])
def encrypt_and_upload():
    file = request.files['file']
    key = generate_key()
    print(key)
    encrypted_file_path = f"encrypted_{file.filename}"
    file.save(encrypted_file_path)
    encrypt_file(encrypted_file_path, key, encrypted_file_path)
    file_id = upload_to_drive(encrypted_file_path)
    os.remove(encrypted_file_path)
    return jsonify({'file_id': file_id})


@app.route('/download-decrypt', methods=['POST'])
def download_and_decrypt():
    file_id = request.form['file_id']
    encrypted_file_path = download_from_drive(file_id)
    key = request.form['key']
    decrypted_file_path = f"decrypted_{os.path.basename(encrypted_file_path)}"
    decrypt_file(encrypted_file_path, key, decrypted_file_path)
    os.remove(encrypted_file_path)
    return jsonify({'decrypted_file_path': decrypted_file_path})


@app.route('/get-all-files', methods=['GET'])
def get_all_files():
    files = get_files_info_from_drive()
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run(debug=True)
