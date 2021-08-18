import sys
import json
import re
import requests
import lxml.html

from encoding import encode_source_url

filename = sys.argv[1]
with open(filename) as f:
    data = json.load(f)

sample_urls = data[0:10]

output = []

for i, url in enumerate(sample_urls):

    r = requests.get(url)
    html = lxml.html.fromstring(r.text)

    json_text = html.xpath('//script[@type="application/ld+json"]/text()')
    if json_text:
        food = re.search(r'"name": "food"', json_text[0])
        recipes = re.search(r'"name": "Recipes"', json_text[0])
        skip_content = [food, recipes]

        if any(skip_content):
            continue

    output.append({
                'source_url': encode_source_url(url),
                'html': lxml.html.tostring(html).decode('utf-8')
            })
    # article_text = html.xpath('//p/text()')
    # page_title = html.xpath('//title/text()')
    # article_text = ''
    # for div in html.cssselect('div.paragraph'):
    #     article_text += ''.join(div.text_content())

    # json_text = html.xpath('//script[@type="application/ld+json"]/text()')
    # if json_text:
    #     food = re.search(r'"name": "food"', json_text[0])
    #     recipes = re.search(r'"name": "Recipes"', json_text[0])
    #     skip_content = [food, recipes]

    #     if any(skip_content):
    #         continue
    #     else:
    #         output.append({
    #             'source_url': url,
    #             'html': lxml.html.tostring(html).decode('utf-8')
    #         })

json.dump(output, sys.stdout, indent=4)
# from pprint import pprint
# pprint(output)
        #video_url = re.search(r'"embedUrl": "(.*?)"', json_text[0]).group(1)
    #     video_metadata = html.xpath('//video')[0].get('data-metadata')
    #     video_url = re.search(r'https:\/\/.*mp4', video_metadata).group(0)
    # if video_url:
    #     print('if video_url')
    #     r = requests.get(video_url, stream=True)
    #     # video_name = re.search(r'videoId=(.*?)', video_url).group(1).replace('=', '-')
    #     # print(video_name)
    #     # video_html = lxml.html.fromstring(r.text)
    #     # # breakpoint()

    #     with open(f'intermediate/articles/video/{i}.mp4', 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=1024):
    #             if chunk:
    #                 f.write(chunk)



        # with open(f'intermediate/articles/video/{i}.mp4', 'wb') as f: 
        #     for chunk in r.iter_content(chunk_size = 1024*1024): 
        #         if chunk: 
        #             f.write(chunk) 