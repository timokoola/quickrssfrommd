# download prompts from gcp bucket
# file name is epoc_timestamp.md
download_prompts:
	# first back up the old prompts to a timestamped file
	cp markdown/prompts.md markdown/prompts.$(shell date +%s).md
	# download the latest prompts
	gsutil cp gs://$(GCP_BUCKET)/prompts.md markdown/prompts.md


generate_feed:
	# generate the feed
	# this will generate a file called feed.xml
	# in the root of the project
	# this file is used by the rss feed
	# to generate the feed
	python3 feed_generator.py	