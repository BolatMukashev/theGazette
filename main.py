from bondua import BounduaParse


if __name__ == '__main__':
    URL = r'https://buondua.com/ugirls-%E2%80%93-ai-you-wu-app-no-2176-bai-zi-yan-%E7%99%BD%E5%AD%90%E5%AB%A3-35-photos-23653'
    asian_girl_photos = BounduaParse(URL, txt=False)
    asian_girl_photos.download_photos()
    asian_girl_photos.crop_all_images()
