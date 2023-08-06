# by RainStar

import os

import requests
from lxml import etree
from urllib import parse

r = requests.get('http://sec.z5x.cn/', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'}).text

p = etree.HTML(r)

# /html/head/meta

url = p.xpath('/html/head/meta/@content')[0].split(';')[-1].split('=')[-1]

host = parse.urlparse(url=url).netloc

os.system('rm -rf pub')
os.system(f'wget --mirror --convert-links --no-parent {url} -P temp')
os.system(f'mv temp/{host} pub')
