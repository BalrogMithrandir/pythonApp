from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("url: http://music.163.com/#/discover/playlist")
bs_obj = BeautifulSoup(html.read(), "html.parser")

text_list = bs_obj.find_all("span")

for text in text_list:
	print(text.get_text())

html.close()
