# download prompts from gcp bucket
# file name is epoc_timestamp.md
download_prompts:
	# first back up the old prompts to a timestamped file
	cp markdown/prompts.md markdown/prompts.$(shell date +%s).md
	# download the latest prompts
	gsutil cp gs://$(GCP_BUCKET)/prompts.md markdown/prompts.md
