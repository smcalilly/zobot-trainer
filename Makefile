GENERATED_FILES = $(shell ls twitter_handles | sed s'/$$/.json/g' | sed s'/^/tweets\//g')

.PHONY: all clean

define get_articles
	for row in $(cat intermediate/articles/links/test.json | jq '.'); do curl ${row}; done
endef

intermediate/articles/html/%.json : intermediate/articles/links/%.json
	mkdir -p $(dir $@)
	cat $< 

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
