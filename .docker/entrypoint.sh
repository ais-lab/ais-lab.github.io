#!/bin/bash

# print folder contents for debugging
printf "\n\nContents:\n\n"
ls

# ensure gems are installed
bundle install

# run cite process
python3 _cite/cite.py

# run jekyll serve 
bundle exec jekyll serve --host=0.0.0.0 --port=4000 --livereload &

# rerun cite process whenever _data files change
watchmedo shell-command \
    --debug-force-polling \
    --recursive \
    --wait \
    --command="python3 _cite/cite.py" \
    --patterns="_data/sources*;_data/orcid*;_data/pubmed*;_data/google-scholar*" &

# Keep container running
tail -f /dev/null