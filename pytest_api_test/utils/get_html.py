# encoding:utf-8
import urllib.request


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
