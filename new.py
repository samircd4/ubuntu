import os
import shutil
import requests

def get_models():
    with open('model.txt') as f:
        lines = f.readlines()
        all_model = []
        for line in lines:
            model = {}
            combine = line.split('\t')
            model['brand'] = combine[0].strip()
            model['name'] = combine[1].strip()
            model['ref'] = combine[2].strip()
            all_model.append(model)

    return all_model


def download_image():# url, id, img_ext
    header = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    print('Downloading image')
    image_url = 'https://cdn2.chrono24.com/images/uhren/28184821-twb5atxz9aeso6ilehqhwdm8-ExtraLarge.jpg'

    img_data = requests.get(image_url, headers=header).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
        print('Image downloaded')
    
download_image()
