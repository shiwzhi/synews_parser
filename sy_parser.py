import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

class Parser(object):
	"""docstring for Parser"""
	def __init__(self, url):
		super(Parser, self).__init__()
		self.url = url
		self.host = urlparse(self.url).netloc
		
		self.html = self.get_html(self.url)
		self.soup = self.get_soup(self.html)
		self.title = self.get_title(self.soup)
		self.pub = self.get_pubulisher(self.soup)
		self.body = self.get_body(self.soup)
		
	
	def remove_special_char(self, text):
		return text.replace('\r', '').replace('\u3000', '')

	def get_html(self, url):
		r = requests.get(url)
		r.encoding = 'utf-8'
		return r.text

	def get_soup(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		return soup

	def get_title(self, soup):
		word = re.compile('biaoti')
		title = soup.find_all('td', re.compile('biaoti'))
		for i in title:
			if len(i.get_text()) > 3:
				return(self.remove_special_char(i.get_text()))

	def get_pubulisher(self, soup):
		try:
			text = soup.find('span', 'STYLE2')
			return self.remove_special_char(text.get_text())
		except Exception as e:
			print(e)
			return ''

# def get_author(soup):
# 	text = soup.find('span', 'STYLE2')
# 	return(remove_special_char(text.get_text().split('发布人：')[1]))

# def get_time(soup):
# 	text = soup.find('span', 'STYLE2')
# 	return(remove_special_char(text.get_text().split('访问次数')[0]))

# def get_view_count(soup):
# 	text = soup.find('span', 'STYLE2').contents[1]['src']
# 	return('http://www.lpssy.edu.cn'+text)

	def get_body(self, soup):
		text = soup.find('td', 'content')
		for j in text.find_all():
			del j['style']
		for i in text.find_all('img'):
			i['src'] = '//'+self.host+i['src']
			del i['width']
			del i['height']
		for k in text.find_all('a'):
			k['href'] = '//'+self.host+k['href']
		return text


