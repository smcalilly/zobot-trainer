import os
import io
from google.cloud import videointelligence

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'zobot-320701-915c0d76bfd0.json'
video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.TEXT_DETECTION]
video_context = videointelligence.VideoContext()

def send(video_paths):
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

        text = ''
        annotation_result = result.annotation_results
        for r in annotation_result:
            for text_annotation in r.text_annotations:
                text += text_annotation.text

        print(text)
    # for text_annotation in annotation_result.text_annotations:
    #     print("\nText: {}".format(text_annotation.text))

    #     # Get the first text segment
    #     text_segment = text_annotation.segments[0]
    #     start_time = text_segment.segment.start_time_offset
    #     end_time = text_segment.segment.end_time_offset
    #     print(
    #         "start_time: {}, end_time: {}".format(
    #             start_time.seconds + start_time.microseconds * 1e-6,
    #             end_time.seconds + end_time.microseconds * 1e-6,
    #         )
    #     )

    #     print("Confidence: {}".format(text_segment.confidence))