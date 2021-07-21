import sys
import json
import re
import requests
import lxml.html

filename = sys.argv[1]
with open(filename) as f:
    data = json.load(f)



sample_urls = data[0:10]
print(sample_urls)

for i, url in enumerate(sample_urls):

    html = requests.get(url)

    doc = lxml.html.fromstring(html.text)
    article_text = doc.xpath('//p/text()')

    json_text = doc.xpath('//script[@type="application/ld+json"]/text()')
    print('json_text')
    print(json_text)
    if json_text:
        food = re.search(r'"name": "food"', json_text[0])
        
        # we don't want food content
        if food:
            continue

        #video_url = re.search(r'"embedUrl": "(.*?)"', json_text[0]).group(1)
        video_metadata = doc.xpath('//video')[0].get('data-metadata')
        video_url = re.search(r'https:\/\/.*mp4', video_metadata).group(0)
    if video_url:
        print('if video_url')
        r = requests.get(video_url, stream=True)
        # video_name = re.search(r'videoId=(.*?)', video_url).group(1).replace('=', '-')
        # print(video_name)
        # video_html = lxml.html.fromstring(r.text)
        # # breakpoint()

        with open(f'intermediate/articles/video/{i}.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)



        # with open(f'intermediate/articles/video/{i}.mp4', 'wb') as f: 
        #     for chunk in r.iter_content(chunk_size = 1024*1024): 
        #         if chunk: 
        #             f.write(chunk) 