import tkinter as tk
from customtkinter import *
from tkinter import filedialog, messagebox, simpledialog, ttk
from encryption import generate_key, encrypt_file, decrypt_file
from drive import upload_to_drive, download_from_drive
import os
import pyperclip

# Globalne zmienne przechowujące wartości wprowadzone przez użytkownika
global_file_id = ""
global_key = ""




def get_encryption_key():
    global global_key
    key = key_entry.get()
    global_key = key.encode() if key else None


def copy_to_clipboard(value):
    pyperclip.copy(value)


def encrypt_and_upload():
    global global_key
    file_path = select_file()
    if file_path:
        key = generate_key()
        global_key = key.decode()
        encrypted_file_path = f"encrypted_{os.path.basename(file_path)}"
        encrypt_file(file_path, key, encrypted_file_path)
        file_id = upload_to_drive(encrypted_file_path)
        os.remove(encrypted_file_path)
        messagebox.showinfo("Encryption Successful",
                            "File uploaded to Drive.\nRemember to save the encryption key and file ID.")
        global global_file_id
        global_file_id = file_id
        file_id_entry.delete(0, tk.END)
        file_id_entry.insert(0, file_id)
        key_entry.delete(0, tk.END)
        key_entry.insert(0, global_key)


def download_and_decrypt():
    global global_file_id, global_key
    file_id = file_id_entry.get()
    if file_id:
        global_file_id = file_id
        get_encryption_key()
        if global_key:
            encrypted_file_path = download_from_drive(global_file_id)
            decrypted_file_path = f"decrypted_{os.path.basename(encrypted_file_path)}"
            decrypt_file(encrypted_file_path, global_key, decrypted_file_path)
            os.remove(encrypted_file_path)
            messagebox.showinfo("Decryption Successful", f"File decrypted and saved as: {decrypted_file_path}")


def copy_file_id():
    global global_file_id
    if global_file_id:
        copy_to_clipboard(global_file_id)


def copy_key():
    global global_key
    if global_key:
        copy_to_clipboard(global_key)


def select_file():
    file_path = filedialog.askopenfilename()
    return file_path


root = CTk()
root.title("File Encryption and Upload to Drive")
root.geometry("500x400")

style = ttk.Style()

set_appearance_mode("dark")


style.configure('TButton', font=('Calibri', 10), padding=5)
style.configure('TLabel', font=('Calibri', 10))


encrypt_button = CTkButton(
    master=root, 
    text="Encrypt and Upload", 
    command=encrypt_and_upload, 
    corner_radius=30, 
    hover_color = "#245e9c"
    )

encrypt_button.pack(pady=10)


decrypt_button = CTkButton(
    master=root, 
    text="Download and Decrypt", 
    command=download_and_decrypt, 
    corner_radius=30, 
    hover_color = "#245e9c"
    )

decrypt_button.pack(pady=10)

file_id_label = CTkLabel(
    master=root, 
    text="File ID: ", 
    corner_radius=30
    )

file_id_label.pack(pady=10)

file_id_entry = CTkEntry(
    master=root, 
    placeholder_text="Here will be the file ID", 
    width=300, 
    corner_radius=30, 
    text_color = "#FFCC70"
    )

file_id_entry.pack(pady=10)

copy_file_id_button = CTkButton(
    master=root, 
    text="Copy File ID", 
    command=copy_file_id, 
    corner_radius=30, 
    hover_color = "#245e9c"
    )

copy_file_id_button.pack(pady=10)


key_label = CTkLabel(
    master=root, 
    text="Encryption Key: ", 
    corner_radius=30
    )

key_label.pack(pady=10)

key_entry = CTkEntry(
    master=root, 
    placeholder_text="Here will be the encryption key", 
    width=300, 
    corner_radius=30, 
    text_color = "#FFCC70"
    )

key_entry.pack(pady=10)

copy_key_button = CTkButton(
    master=root, 
    text="Copy Key", 
    command=copy_key, 
    corner_radius=30, 
    hover_color = "#245e9c"
    )

copy_key_button.pack(pady=10)

root.mainloop()
