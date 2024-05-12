from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_file(file_path, key, encrypted_file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(encrypted_file_path, key, decrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
