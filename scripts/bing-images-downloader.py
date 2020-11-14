#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
import base64

keyword = input('What do you want? ')

save_floder = input('Where do you want to save images?(Default as the current directory) ')
if save_floder == '': save_floder = os.getcwd()
if not os.path.exists(save_floder): os.mkdir(save_floder)

url = 'https://cn.bing.com/images/search?q=%s&form=BESBTB&first=1&scenario=ImageBasicHover&ensearch=1' % keyword
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}

print('Starting fetching image urls...')
r = requests.get(url, headers=headers)
html = r.text
soup = BeautifulSoup(html, 'lxml')
img_elements = soup.select('.mimg')

img_urls = []
for img_element in img_elements:
    if 'src' in img_element.attrs:
        img_urls.append(img_element['src'])
    if 'data-src' in img_element.attrs:
        img_urls.append(img_element['data-src'])

print('Starting downloading images...')
for i in range(len(img_urls)):
    
    if 'data:image/' in img_urls[i]:
        print('Warning: Not support base64')
        continue
        # img_urls[i] += (4 - len(img_urls[i]) % 4) * '='
        # img_bytes = base64.b64decode(img_urls[i].split(',')[1])
        # file_name = save_floder + '/' + str(i) + '.' + img_urls[i].split(';')[0].split('/')[1]
    else:
        r = requests.get(img_urls[i])
        img_bytes = r.content
        file_name = save_floder + '/' + str(i) + '.' + r.headers['Content-Type'].split('/')[1]
    
    with open(file_name, 'wb') as f:
        f.write(img_bytes)
    print('Downloaded %s' % file_name)
