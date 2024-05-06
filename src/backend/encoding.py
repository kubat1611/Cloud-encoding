import tkinter as tk
from tkinter import filedialog
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from cryptography.fernet import Fernet
import os


class CloudEncryptorApp:
    def __init__(self, master):
        self.master = master
        master.title("Cloud Encryptor")

        self.label = tk.Label(master, text="Select a file to encrypt and upload to Google Drive:")
        self.label.pack()

        self.select_file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_file_button.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt & Upload", command=self.encrypt_and_upload,
                                        state=tk.DISABLED)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Download & Decrypt", command=self.download_and_decrypt,
                                        state=tk.DISABLED)
        self.decrypt_button.pack()

        self.key = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.encrypt_button.config(state=tk.NORMAL)

    def generate_key(self):
        self.key = Fernet.generate_key()

    def encrypt_file(self, file_path, encrypted_file_path):
        with open(file_path, 'rb') as file:
            data = file.read()

        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data)

        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

    def upload_to_google_drive(self, file_path):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        file_name = os.path.basename(file_path)
        file_to_upload = drive.CreateFile({'title': file_name})
        file_to_upload.SetContentFile(file_path)
        file_to_upload.Upload()
        return file_to_upload['id']

    def encrypt_and_upload(self):
        self.generate_key()
        encrypted_file_path = "encrypted_data.txt"
        self.encrypt_file(self.file_path, encrypted_file_path)
        self.file_id = self.upload_to_google_drive(encrypted_file_path)
        self.label.config(text=f"File encrypted and uploaded with ID: {self.file_id}")
        self.encrypt_button.config(state=tk.DISABLED)
        self.decrypt_button.config(state=tk.NORMAL)

    def download_from_google_drive(self, file_id):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        file_to_download = drive.CreateFile({'id': file_id})
        downloaded_file_path = "downloaded_encrypted_data.txt"
        file_to_download.GetContentFile(downloaded_file_path)
        return downloaded_file_path

    def decrypt_file(self, encrypted_file_path, decrypted_file_path):
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

    def download_and_decrypt(self):
        decrypted_file_path = "decrypted_data.txt"
        downloaded_file_path = self.download_from_google_drive(self.file_id)
        self.decrypt_file(downloaded_file_path, decrypted_file_path)
        self.label.config(text=f"File downloaded and decrypted: {decrypted_file_path}")
        os.remove(downloaded_file_path)
        self.decrypt_button.config(state=tk.DISABLED)


root = tk.Tk()
app = CloudEncryptorApp(root)
root.mainloop()
