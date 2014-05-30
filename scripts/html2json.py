# coding=utf-8

from lxml import etree


parser = etree.HTMLParser()
html = etree.parse('lemmata.html', parser)

rows = html.xpath('//table')[0].findall('tr')

for row in rows:
    cols = row.findall('td')
    if len(cols) == 4:
        print cols[0].text, cols[1].text
        meaning = [c.text for c in cols[3].findall('ol/li')]
        print meaning
        print "\n\n"

