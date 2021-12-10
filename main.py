from bondua import BounduaParse

if __name__ == '__main__':
    URL = r'https://buondua.com/mfstar-vol-233-zhu-ke-er-flower-%E6%9C%B1-%E5%8F%AF-%E5%84%BF-78-pictures-17999'
    asian_girl_photos = BounduaParse(URL)
    asian_girl_photos.download_photos()
    asian_girl_photos.crop_all_images()
