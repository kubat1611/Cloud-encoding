import requests

url = 'http://localhost:5000/download-decrypt'
data = {
    'file_id': '1UFnVOXs6-H8tNBdm99gn-60oMUPBbHFs',
    'key': 'hYo1hkY2TmZFlYmNekyLuswdplls2hj9mP-B9BuN_cs='
}
response = requests.post(url, data=data)

if response.status_code == 200:
    decrypted_file_path = response.json()['decrypted_file_path']
    print("File downloaded and decrypted successfully.")
    print("Decrypted file path:", decrypted_file_path)
else:
    print("Error:", response.text)
