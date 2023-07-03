from bondua import BounduaParse, ImageCroping

"""
https://buondua.com/lilynah-lw067-sunhye-%EC%84%A0%ED%98%9C-vol-01-51-photos-30905
https://buondua.com/espacia-korea-ehc-120-yua-51-photos-30894
https://buondua.com/espacia-korea-ehc-109-somi-%EC%86%8C%EB%AF%B8-50-photos-30879
"""

if __name__ == '__main__':
    URL = r'https://buondua.com/espacia-korea-ehc-109-somi-%EC%86%8C%EB%AF%B8-50-photos-30879'
    #asian_girl_photos = BounduaParse(URL, txt=False)
    #asian_girl_photos.download_photos()
    #asian_girl_photos.crop_all_images(y1=0,y2=25)
    my_images = ImageCroping("C:\\Users\\bolat\\Desktop\\my_programs\\theGazette\\photos\\[Lilynah] LW067 Sunhye (선혜) Vol.01 (51 photos)")
    #my_images.crop_all_images(y1=50,y2=85)
    # sizes = my_images.get_sizes()
    # print(sizes)
