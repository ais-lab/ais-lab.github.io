# start with official ruby docker image as base
FROM ruby:3.1.2

# set working directory within container
WORKDIR /usr/src/app

# pull in ruby (jekyll) and python (cite process) package info
COPY Gemfile Gemfile.lock _cite/requirements.txt ./

# install dependencies for nokogiri and ffi
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    zlib1g-dev

# install ruby packages - 修正部分
RUN VERSION=$(grep -A 1 'BUNDLED WITH' Gemfile.lock | tail -n 1 | xargs); \
    gem install bundler --version ${VERSION} && \
    bundle config set --local path 'vendor/bundle' && \
    bundle _${VERSION}_ install

# install python
RUN apt update && apt install -y python3 python3-pip

# install python packages
RUN python3 -m pip install --no-cache-dir --upgrade --requirement requirements.txt

# install python package for listening for file changes
RUN pip install "watchdog[watchmedo]==3.0.0"

# ports used by jekyll
EXPOSE 4000
EXPOSE 35729

# run jekyll and cite process
COPY .docker/entrypoint.sh /var/entrypoint.sh
RUN chmod +x /var/entrypoint.sh
CMD [ "/var/entrypoint.sh" ]