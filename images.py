from PIL import Image
import requests
from bs4 import BeautifulSoup



def imreverse():
    im = Image.open('savedimage.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            pixels[i, j] = (256 - pixels[i, j][0], 256 - pixels[i, j][1], 256 - pixels[i, j][2])
    im.save('res.jpg')

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def parser(x, y):
    url = 'https://chemequations.com/ru/?s=' + x + '+%2B+' + y + '&ref=input'


    def get_html(url, params=None):
        r = requests.get(url, params=params)
        return r


    def get_content(html):
        global c
        s = BeautifulSoup(html, 'html.parser')
        pog = s.find('h1', class_='equation main-equation well').get_text()
        return pog


    def parse():
        html = get_html(url)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            print('Error')

    return parse()


def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r


def chain(text):
    def get_content(html):
        global y
        s = BeautifulSoup(html, 'html.parser')
        react = s.findAll('div', class_='reac')
        for r in react:
            reaction = r.get_text()
            el = str(reaction).split('→')
            el = str(reaction).split('+')
            el = str(reaction).split()
            if el[0] == x or el[2] == x:
                totr = reaction
                break
        try:
            return totr
        except:
             return '?'


    def parse():
        html = get_html(url)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            print('Error')


    out = []
    c = 0
    a = list(text.split())
    for i in range(len(a) - 1):
        c += 1
        print(out)
        x = a[i]
        y = a[i + 1]
        url = 'https://tutata.ru/chemistry/search?s=%3D+' + y
        res = parse()
        if len(res) == 1:
            out.append(str(c) + ':  ' + '?')
        else:
            out.append(str(c) + ':  ' + ''.join(res)[1:])
    return out
