import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


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
