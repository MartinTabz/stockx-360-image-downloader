import os
import requests
from slugify import slugify

web_content = input("Paste the URL of the first image: ")
name = input("Name of the folder containing images: ")

splitted = web_content.split("/img")

script_directory = os.path.dirname(os.path.abspath(__file__))
downloads_directory = os.path.join(script_directory, 'Downloads')

os.makedirs(downloads_directory, exist_ok=True)

new_folder_path = os.path.join(downloads_directory, name)

unique_folder_path = new_folder_path
counter = 1
while os.path.exists(unique_folder_path):
    unique_folder_path = f"{new_folder_path}_{counter}"
    counter += 1

os.makedirs(unique_folder_path)

for x in range(1,37):
    down_url = ""
    if x < 10:
        down_url = splitted[0] + "/img0" + str(x) + ".jpg"
    else:
        down_url = splitted[0] + "/img" + str(x) + ".jpg"
    
    response = requests.get(down_url)
    if response.status_code == 200:
        file_name = f"{x}_sneaker_{slugify(name)}.jpg"
        if x < 10:
            file_name = f"0{x}_sneaker_{slugify(name)}.jpg"
        file_path = os.path.join(unique_folder_path, file_name)
        
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image number {x} downloaded")
    else:
        print(f"Wasnt able to download image: {down_url}")

print(f"Images were downloaded to: {unique_folder_path}")