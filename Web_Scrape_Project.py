#Written 10/24/2019 TDR
from gazpacho import get, Soup
import pandas as pd

from urllib.request import urlopen

url = 'http://registration.baa.org/2019/cf/Public/iframe_TopFinishers.htm'
html = urlopen(url)
response = get(url)
soup = Soup(response)
df = pd.read_html(str(soup.find('table')))
print(df)

import re

list_rows = []

df = pd.DataFrame(list_rows)
df.head(10)
