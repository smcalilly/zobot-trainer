import sys
import json
import re
import os
import io
import requests
import lxml.html
from google.cloud import videointelligence



# filename = sys.argv[1]
# with open(filename) as f:
#     data = json.load(f)

video_paths = ['intermediate/articles/video/https%3Abackslashbackslasht-cobackslashF396fjiosa.mp4']

# for article in data:
#     html = lxml.html.fromstring(article['html'])
#     try:
#         video_metadata = html.xpath('//video')[0].get('data-metadata')
#         video_url = re.search(r'https:\/\/.*mp4', video_metadata).group(0)
#         if video_url:
#             r = requests.get(video_url, stream=True)

#             source_article_url = article['source_url']
#             mp4_path = f'intermediate/articles/video/{source_article_url}.mp4'

#             with open(mp4_path, 'wb') as f:
#                 for chunk in r.iter_content(chunk_size=1024):
#                     if chunk:
#                         f.write(chunk)
#             video_paths.append(mp4_path)
#     except IndexError:
#         pass

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'zobot-320701-915c0d76bfd0.json'
video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.TEXT_DETECTION]
video_context = videointelligence.VideoContext()


for v in video_paths:
    with io.open(v, 'rb') as f:
        input_content = f.read()

    operation = video_client.annotate_video(
    request={
        'features': features,
        'input_content': input_content,
        'video_context': video_context,
    })

    print("\nProcessing video for text detection.")
    result = operation.result(timeout=300)

    # The first result is retrieved because a single video was processed.
    annotation_result = result.annotation_results[0]

for text_annotation in annotation_result.text_annotations:
    print("\nText: {}".format(text_annotation.text))

    # Get the first text segment
    text_segment = text_annotation.segments[0]
    start_time = text_segment.segment.start_time_offset
    end_time = text_segment.segment.end_time_offset
    print(
        "start_time: {}, end_time: {}".format(
            start_time.seconds + start_time.microseconds * 1e-6,
            end_time.seconds + end_time.microseconds * 1e-6,
        )
    )

    print("Confidence: {}".format(text_segment.confidence))

    # Show the result for the first frame in this segment.
    frame = text_segment.frames[0]
    time_offset = frame.time_offset
    print(
        "Time offset for the first frame: {}".format(
            time_offset.seconds + time_offset.microseconds * 1e-6
        )
    )

