import json
from telegraph import Telegraph


def get_token():
    with open('telegraph_token.json') as f:
        data = json.load(f)
    return data


token = get_token()
telegraph = Telegraph(token['access_token'])


class TelegraphClient(object):
    def __init__(self):
        self.short_name = 'kazashki_qyzdar'  # обязательно - имя ученой записи
        self.author_name = 'journal \"Naked Asia\"'  # не обязательно
        self.author_url = 'https://t.me/kazashki_qyzdar'  # не обязательно
        self.token_file_name = 'telegraph_token.json'

    def create_account(self):
        access_data = telegraph.create_account(short_name=self.short_name,
                                               author_name=self.author_name,
                                               author_url=self.author_url)
        with open(self.token_file_name, 'w', encoding='utf-8') as file:
            json.dump(access_data, file, ensure_ascii=False, indent=4)

    def create_page(self, title, html_content="<p>Hello, world!</p><img scr='photos/XIUREN No.3388 Zheng Ying Shan ("
                                              "郑颖姗Bev) (49 photos)/1.jpg' alt=''>"):
        page = telegraph.create_page(title=title, html_content=html_content, author_name=self.author_name,
                                     author_url=self.author_url, return_content=True)
        print(page)


if __name__ == '__main__':
    client = TelegraphClient()
    client.create_page('Привет')
