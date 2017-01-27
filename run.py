from flask import Flask, flash, redirect, render_template, request, session, url_for, make_response
import requests
from bs4 import BeautifulSoup
import sy_parser



app = Flask(__name__)


@app.route("/s/")
def parse():
	url = "http://www.lpssy.edu.cn/s/1/t/1/88/0a/info34826.htm"
	parsed = sy_parser.Parser(url)
	return render_template('index.html', content=parsed)


if __name__ == '__main__':
	app.run(host = '0.0.0.0')