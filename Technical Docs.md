# Dokumentacja techniczna: Cloud-encoding

## 1. Wstęp

Aplikacja została stworzona w celu umożliwienia szyfrowania plików przy użyciu algorytmu Fernet z biblioteki cryptography, a następnie przesyłania ich na dysk Google Drive. Interfejs graficzny oparty jest na bibliotece Tkinter, co umożliwia łatwe korzystanie z aplikacji.

## 2. Funkcje aplikacji

### 2.1 Szyfrowanie plików

Użytkownik może wybrać plik, który chce zaszyfrować, a następnie aplikacja generuje klucz i szyfruje plik przy użyciu algorytmu Fernet. Zaszyfrowany plik jest następnie przesyłany na dysk Google Drive.

### 2.2 Deszyfrowanie plików

Użytkownik może podać identyfikator pliku z dysku Google Drive oraz klucz szyfrowania, aby pobrać zaszyfrowany plik, zdekodować go przy użyciu algorytmu Fernet i zapisać w formie pliku odszyfrowanego.

### 2.3 Kopiowanie identyfikatora pliku i klucza szyfrowania

Aplikacja umożliwia kopiowanie identyfikatora pliku oraz klucza szyfrowania za pomocą przycisków.

## 3. Struktura kodu

### 3.1 Pliki źródłowe

- **ui.py**: Główny plik aplikacji, który definiuje interfejs graficzny i obsługuje logikę aplikacji.
- **encryption.py**: Plik zawierający funkcje do szyfrowania i deszyfrowania plików.
- **drive.py**: Plik zawierający funkcje do przesyłania plików na dysk Google Drive.

### 3.2 Wykorzystane biblioteki

- **Tkinter** i **customtkinter**: Biblioteka do tworzenia interfejsu graficznego.
- **cryptography**: Biblioteka do szyfrowania plików.
- **pydrive**: Biblioteka do interakcji z Google Drive.
- **os** Bibliotek do wybierania plików z systemu

## 4. Instrukcje instalacji

### 4.1 Wymagania

- Python 3.x
- Biblioteki: cryptography, pydrive, os,Tkinter, customtkinter

### 4.2 Instalacja zależności
pip install -r .\requirements

