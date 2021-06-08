import discord
from PIL import Image
import requests
from bs4 import BeautifulSoup
import random as ran
import string
import ast

def imreversep():
    im = Image.open('savedimage.png')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            pixels[i, j] = (256 - pixels[i, j][0], 256 - pixels[i, j][1], 256 - pixels[i, j][2])
    im.save('res.png')


def imreversej():
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
            z = el[0]
            z1 = el[2]
            if z == x or el[2] == x or z[1:] == x or z1[1:] == x:
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
            return 'Error'


    out = []
    c = 0
    a = list(text.split())
    for i in range(len(a) - 1):
        c += 1
        x = a[i]
        y = a[i + 1]
        for j in range(10):
            url = 'https://tutata.ru/chemistry/search?s=%3D+' + y + '&page=' + str(j)
            res = parse()
            if res != '?' or res == 'Error':
                break
        if len(res) == 1:
            out.append(str(c) + ':  ' + '?')
        else:
            out.append(str(c) + ':  ' + ''.join(res)[1:])
    return out


def makeanagliphp(delta):

    im = Image.open(r'C:\Users\anubis\PycharmProjects\discordbot\lol.png')
    pixels = im.load()
    x, y = im.size

    for i in range(x):
        for j in range(y):
            if i > delta and j > delta:
                pixels[i - delta, j - delta] = (pixels[i, j][0], pixels[i - delta,
                                                                        j - delta][1], pixels[i - delta, j - delta][2])
    im.save("pc.png")


def makeanagliphj(delta):

    im = Image.open(r'C:\Users\anubis\PycharmProjects\discordbot\lol.jpg')
    pixels = im.load()
    x, y = im.size

    for i in range(x):
        for j in range(y):
            if i > delta and j > delta:
                pixels[i - delta, j - delta] = (pixels[i, j][0], pixels[i - delta,
                                                                        j - delta][1], pixels[i - delta, j - delta][2])
    im.save("pc.jpg")


def gradientw():
    ni = Image.new('RGB', (512, 200), (0, 0, 0))
    pix = ni.load()
    n = [ran.randint(150, 255), ran.randint(150, 255), ran.randint(150, 255)]
    n[ran.randint(0, 2)] = 0
    r = n[0]
    g = n[1]
    b = n[2]
    for i in range(512):
        if i % 2 == 0:
            if r < 255:
                r += 1
            if g < 255:
                g += 1
            if b < 255:
                b += 1
        for j in range(200):
            f = (r, g, b)
            pix[i, j] = f
    ni.save("gr.png")
    return (tuple(n))


def gradientb():
    ni = Image.new('RGB', (512, 200), (0, 0, 0))
    pix = ni.load()
    n = [ran.randint(150, 255), ran.randint(150, 255), ran.randint(150, 255)]
    n[ran.randint(0, 2)] = 0
    r = n[0]
    g = n[1]
    b = n[2]
    for i in range(512):
        if i % 2 == 0:
            if r > 0:
                r -= 1
            if g > 0:
                g -= 1
            if b > 0:
                b -= 1
        for j in range(200):
            f = (r, g, b)
            pix[i, j] = f
    ni.save("gr.png")
    return(tuple(n))

def emtranslate(text):
    d = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
         '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
    a = []
    text = list(text)
    for i in text:
        if i in string.ascii_letters:
            a.append(':regional_indicator_' + i + ':')
        elif i in string.digits:
            a.append(':' + d[str(i)] + ':')
        else:
            a.append(':blue_square:')
    return a



class Sendembed:
    def __init__(self, ctx, channel):
        self.author = ctx.message.author
        self.title = ''
        self.description = ''
        self.footer = ''
        self.thumbnail = False
        self.image = False
        self.author = ctx.message.author
        self.channel = channel

    def check(self, channel):
        if channel == self.channel:
            return True
        return False

    def ccheck(self, content):
        if content.startswith('title:'):
            self.title = content[7:]
            print(self.title)
        elif content.startswith('description:'):
            self.description = content[13:]
        elif content.startswith('footer:'):
            self.footer = content[8:]
        elif content.startswith('thumbnail:'):
            self.thumbnail = content[11:]
        elif content.startswith('image:'):
            self.image = content[7:]
        elif content.startswith('channel:'):
            self.channel = int(content[9:])
        elif content.startswith('done'):
            emb = discord.Embed(
                title=self.title,
                description=self.description,
            )
            emb.set_footer(
                text=self.footer,
                icon_url=self.author.avatar_url
            )
            if self.image:
                emb.set_image(
                    url=self.image
                )
            if self.thumbnail:
                emb.set_thumbnail(
                    url=self.thumbnail
                )
            return emb

    def __call__(self):
        print(self.channel)
        return self.channel
