import os

from cryptography.fernet import Fernet
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def generate_key():
    return Fernet.generate_key()


def encrypt_file(file_path, key, encrypted_file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def upload_to_drive(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_name = os.path.basename(file_path)
    file_to_upload = drive.CreateFile({'title': file_name})
    file_to_upload.SetContentFile(file_path)
    file_to_upload.Upload()
    return file_to_upload['id']


def download_from_drive(file_id):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_to_download = drive.CreateFile({'id': file_id})
    downloaded_file_path = "downloaded_encrypted_data.txt"
    file_to_download.GetContentFile(downloaded_file_path)
    return downloaded_file_path


def decrypt_file(encrypted_file_path, key, decrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)