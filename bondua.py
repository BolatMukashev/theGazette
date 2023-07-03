import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm as loading_bar
from PIL import Image
from pathlib import Path


fucked_file = 'Thumbs.db'


class BounduaParse(object):

    def __init__(self, url, txt=False):
        self.url = url
        self.headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 ('
                                      'KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
                                      'accept': '*/*'}
        self.title = None
        self.pages_numbers = 1
        self.all_photos_links = []
        self.directory = None
        self.txt = txt
        self.parse()

    def get_html(self, params=None):
        response = requests.get(url=self.url, headers=self.headers, params=params)
        return response

    @staticmethod
    def get_page(html):
        soup = BeautifulSoup(html.text, 'html5lib')             # 'lxml'
        # print(soup.prettify())
        return soup

    @staticmethod
    def get_title(page):
        image_block = page.find('div', class_='article-header')
        h1_text = image_block.h1.text
        finally_title = h1_text.replace(':', '')
        return finally_title

    def get_first_page(self):
        html = self.get_html()
        page = self.get_page(html)
        return page

    def get_pages_numbers(self, page):
        pagination_block = page.find('div', class_='pagination-list')
        blocks = pagination_block.find_all('span')
        self.pages_numbers = len(blocks)

    @staticmethod
    def get_photos_links(page):
        photos_block = page.find('div', class_='article-fulltext')
        items = photos_block.find_all('img')
        urls = [x.get('src') for x in items]
        print(urls)
        return urls

    def get_all_photos(self):
        all_photos = []
        for x in range(1, self.pages_numbers + 1):
            html = self.get_html(params={'page': x})
            page_ = self.get_page(html)
            photos = self.get_photos_links(page_)
            all_photos.extend(photos)
        return all_photos

    def parse(self):
        first_page = self.get_first_page()
        self.title = self.get_title(first_page)
        self.get_pages_numbers(first_page)
        self.all_photos_links = self.get_all_photos()
        self.directory = os.path.join(os.getcwd(), 'photos', self.title)

    @staticmethod
    def create_directory(name):
        path = os.path.join(os.getcwd(), 'photos', name)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        finally:
            return path

    def download_photos(self):
        self.directory = self.create_directory(self.title)
        count = 1
        for link in loading_bar(self.all_photos_links, desc='Скачиваю фотки'):
            try:
                img_data = requests.get(link, headers=self.headers).content
                photo_path = os.path.join(self.directory, f'{count}.jpg')
                with open(photo_path, 'wb') as photo:
                    photo.write(img_data)
                count += 1
            except Exception as exx:
                print(exx)
        self._delete_file()


class ImageCroping:
    def __init__(self, path):
        self.path = path
        self.all_photos = Path(self.path).iterdir()

    @staticmethod
    def crop_image(photo_path, x1: int, x2: int, y1: int, y2: int):
        image = Image.open(photo_path)
        width, height = image.size
        crop_left, crop_top = x1, y1
        crop_right = width - x2
        crop_bottom = height - y2
        cropped = image.crop((crop_left, crop_top, crop_right, crop_bottom))
        cropped.save(photo_path)

    def crop_all_images(self, x1=0, x2=0, y1=0, y2=0):
        self._delete_file()
        for photo in loading_bar(self.all_photos, desc='Образаю фотки'):
            self.crop_image(photo, x1, x2, y1, y2)

    @staticmethod
    def get_img_size(img_path: Path):
        im = Image.open(img_path)
        return im.size

    def get_sizes(self):
        li = []
        for photo in self.all_photos:
            ph = self.get_img_size(photo)
            li.append(ph)
        return set(li)

    def _delete_file(self, file_name=fucked_file):
        if os.path.isfile(os.path.join(self.path, file_name)):
            os.remove(os.path.join(self.path, file_name))

