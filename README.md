# zobot trainer
an abandoned attempt to train openai's gpt-3 to summarize online content into short text for video. 

this pipeline scrapes the most recent tweets from the twitter accounts of southern living and food & wine. then, the pipeline scrapes the articles and downloads the videos. the last missing piece: extract the text out of the video and use that as the expect output for gpt-3, and use the article text as the input. i've tried a few easy ways of doing this (pardon the mess), but none of them work well. it's gonna take some effort to get the text from each frame in the video, and i currently don't have the time. so should somebody find this repo, they should do it!

## setup python environment
A dependency needs 3.8...
- pip
- python
- pyenv

## steps
- download tweets
- get articles and videos
- parse articles into text for the prompt_text
- extract text from videos, for the completion_text
- combine the prompt_text and completion_text dependencies