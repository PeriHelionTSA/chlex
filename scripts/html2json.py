# coding=utf-8

from lxml import etree


parser = etree.HTMLParser()
html = etree.parse('lemmata.html', parser)

rows = html.xpath('//tr')

for row in rows:
    for idx, col in enumerate(row.xpath('//td')):
        print col.text
  
        if idx % 3: 
            for meaning in col.xpath('ol//li'):
                print meaning.text
