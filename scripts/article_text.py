import sys
import json
import lxml.html


filename = sys.argv[1]

output = []

with open(filename) as f:
    data = json.load(f)

for article in data:
    html = lxml.html.fromstring(article['html'])

    article_text = html.xpath('//p/text()')
    article_text = ''
    for div in html.cssselect('div.paragraph'):
        article_text += ''.join(div.text_content())

    output.append({
        'source_url': article['source_url'],
        'text': article_text
    })

json.dump(output, sys.stdout)