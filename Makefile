GENERATED_FILES = $(shell ls twitter_handles | sed s'/$$/.json/g' | sed s'/^/tweets\//g')

.PHONY: all clean

define get_articles
	for row in $(cat intermediate/articles/links/test.json | jq '.'); do curl ${row}; done
endef

trainer : $(GENERATED_FILES)
	python3 scripts/train_gpt3.py

output/gpt_training.json : intermediate/extracted/video_and_article_text/.%json
	echo

intermediate/extracted/video_and_article_text/.%json : intermediate/articles/source_video/%.json intermediate/articles/article_text/%.json 
	echo

intermediate/articles/video_text/%.json : intermediate/articles/source_video/%.json
	echo

intermediate/articles/video_text/%.json : intermediate/articles/raw_html/%.json
	python3 scripts/extract_video.py

intermediate/articles/article_text/%.json : intermediate/articles/raw_html/%.json
	python3 scripts/article_text.py $< > $@

intermediate/articles/raw_html/%.json : intermediate/articles/links/%.json
	mkdir -p $(dir $@)
	python3 scripts/get_html.py $< > $@

intermediate/articles/links/%.json : intermediate/tweets/content/%.json
	mkdir -p $(dir $@)
	python3 scripts/get_links.py $< > $@
	# cat $< | grep -Eo 'https:\/\/[^ >]+' | sed s'/",//g' | sed s'/"//g' > $@

intermediate/tweets/content/%.json : intermediate/tweets/json/%.json
	mkdir -p $(dir $@)
	cat $< | jq '.[].content' | jq -s '.'  > $@

intermediate/tweets/json/%.json : twitter_handles/%
	mkdir -p $(dir $@)
	snscrape --jsonl --since 2021-07-01 twitter-user $(notdir $<) | jq -s '.' > $@
