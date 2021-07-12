import requests
import urllib.request
import pandas as pd

from requests.exceptions import MissingSchema

from bs4 import BeautifulSoup

BASE_PATH = '/Users/seansmith/GLP-Group-1-21/src/train/data/'
DATA_PATH = BASE_PATH + 'ralph_lauren_retail_feed.csv'
OUT_PATH = BASE_PATH + 'Images/'


def scrap_images(data_path):
    df = pd.read_csv(data_path)
    for i in range(len(df)):
        html_page = requests.get(df['url'][i])
        soup = BeautifulSoup(html_page.content, 'html.parser')
        
        images = [img.get('data-img') for img in soup.findAll('img') if img]

        if images is None:
            continue

        # setting filename and image URL
        prod_type = df['product_type'][i]
        sku = df['sku'][i]
        filename = OUT_PATH + prod_type + '_' + sku + '.jpg'


        image_url = images[0]
        # calling urlretrieve function to get resource
        try:
            response = requests.get(image_url)

            with open(filename, 'wb') as file:
                file.write(response.content)
        except MissingSchema:
            print(filename + ': No image available!')


if __name__ == '__main__':
    scrap_images(DATA_PATH)
