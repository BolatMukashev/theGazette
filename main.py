from bondua import BounduaParse


if __name__ == '__main__':
    URL = r'https://buondua.com/leehee-express-lebe-023a-b-so-92-photos-23798'
    asian_girl_photos = BounduaParse(URL, txt=False)
    asian_girl_photos.download_photos()
    asian_girl_photos.crop_all_images()
