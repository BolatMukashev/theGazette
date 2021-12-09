from bondua import BounduaParse

if __name__ == '__main__':
    URL = r'https://buondua.com/xiuren-no-3388-zheng-ying-shan-%E9%83%91%E9%A2%96%E5%A7%97bev-49-photos-23286'
    asian_girl_photos = BounduaParse(URL)
    asian_girl_photos.download_photos()
