from bondua import BounduaParse

if __name__ == '__main__':
    URL = r'https://buondua.com/huayang-vol-408-zhu-ke-er-%E6%9C%B1%E5%8F%AF%E5%84%BFflower-57-photos-22886'
    asian_girl_photos = BounduaParse(URL)
    asian_girl_photos.download_photos()
