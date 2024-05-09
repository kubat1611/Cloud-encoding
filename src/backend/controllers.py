import os
from datetime import datetime

from cryptography.fernet import Fernet
from flask import jsonify
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


def get_files_info_from_drive():
    # Autoryzacja Google Drive
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.json")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("credentials.json")

    drive = GoogleDrive(gauth)

    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    print(file_list)
    files_info = []
    for file in file_list:
        file_size = file.get('fileSize', 'Unknown')
        file_type = 'file' if file['kind'] == 'drive#file' and file_size != 'Unknown' else 'folder'

        file_info = {
            'id': file['id'],
            'name': file['title'],
            'size': file_size,
            'type': file_type,
            'last_used_time': datetime.strptime(file['modifiedDate'],
                                                "%Y-%m-%dT%H:%M:%S.%fZ") if 'modifiedDate' in file else None
        }
        files_info.append(file_info)

    return files_info

