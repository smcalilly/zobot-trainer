# import speech_recognition as sr 
# import moviepy.editor as mp
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# num_seconds_video= 120
# print("The video is {} seconds".format(num_seconds_video))
# l=list(range(0,num_seconds_video+1,60))

# diz={}


from videocr import get_subtitles

if __name__ == '__main__':
    video_path = 'intermediate/articles/video/https%3Abackslashbackslasht-cobackslashF396fjiosa.mp4'

    subtitles = get_subtitles(video_path, lang='eng', time_start='0:00', time_end='0:20',
                              conf_threshold=65, sim_threshold=90, use_fullframe=False)
    print(subtitles)


# for i in range(len(l)-1):
#     ffmpeg_extract_subclip(video_path, l[i]-2*(l[i]!=0), l[i+1], targetname="chunks/cut{}.mp4".format(i+1))
#     clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i+1)) 
#     clip.audio.write_audiofile(r"converted/converted{}.wav".format(i+1))
#     r = sr.Recognizer()
#     audio = sr.AudioFile("converted/converted{}.wav".format(i+1))
#     with audio as source:
#         r.adjust_for_ambient_noise(source)  
#         audio_file = r.record(source)
#     result = r.recognize_google(audio_file)
#     diz['chunk{}'.format(i+1)]=result

# l_chunks=[diz['chunk{}'.format(i+1)] for i in range(len(diz))]
# text='\n'.join(l_chunks)

# print("Recognized Speech:") 
# print("\n") 
# print(text) 
# print("Finally ready!")