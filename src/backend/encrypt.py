import requests

url = 'http://localhost:5000/encrypt-upload'
files = {'file': open('file_to_encrypt.txt', 'rb')}
response = requests.post(url, files=files)

if response.status_code == 200:
    print("File encrypted and uploaded successfully.")
    print("File ID on Google Drive:", response.json()['file_id'])
else:
    print("Error:", response.text)
# 15uCjUtGVLff-WihXilh3tl0G2hmPHi_l