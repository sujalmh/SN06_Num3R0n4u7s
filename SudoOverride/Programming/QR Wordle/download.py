import requests
import os

def download_images(save_path):
    # Create the directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Open the URL in the browser
    for i in range(64):
        img_no=str(i)
        url="https://qr.sudooverride.tech/img.php?img="+img_no
        save=save_path+"part-"+img_no+".jpg"
        response = requests.get(url)
        if response.status_code:
            fp = open(save, 'wb')
            fp.write(response.content)
            fp.close()

url = "https://qr.sudooverride.tech/"
save_path = "images/"

download_images(save_path)
