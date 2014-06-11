# coding=utf-8

from lxml import etree

import sys
import codecs
import locale
import unicodedata

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)


parser = etree.HTMLParser()
html = etree.parse('lemmata.html', parser)

rows = html.xpath('//table')[0].findall('tr')

LEM_JSON = u"""{{
    "fields": {{
        "comment": {},
        "graphs": "{}",
        "pinyin": "{}"
    }},
    "model": "common.lem",
    "pk": {}
}}"""

MEANING_JSON = u"""{{
    "fields": {{
        "meaning": {},
        "lem": {}
     }},
     "model": "common.meaning",
     "pk": {}
}}"""

lem_pk = 1
meaning_pk = 1

print "["

for row in rows:
    cols = row.findall('td')
    if len(cols) == 4:
        if lem_pk > 1:
            print ","
        pinyin = cols[0].text
        graphs = cols[1].text
        comment = cols[2].text
        if comment == None:
            comment = u"null"
        else:
            comment = "".join(ch for ch in unicode(comment) if unicodedata.category(ch)[0] != "C")
            comment = "\"" + comment.replace('"', '') + "\""

        print LEM_JSON.format(unicode(comment), unicode(graphs), unicode(pinyin), lem_pk)
        meaning = [c.text for c in cols[3].findall('ol/li')]
        meaning_loop = 0
        if meaning:
            for m in meaning:
                print ","
                m = "".join(ch for ch in unicode(m) if unicodedata.category(ch)[0] != "C")
                m = "\"" + m.replace('"', '') + "\""
                print MEANING_JSON.format(unicode(m), lem_pk, meaning_pk)
                meaning_pk += 1

        #print meaning
        #print "\n\n"
        lem_pk += 1

print "]"
