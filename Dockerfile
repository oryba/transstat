FROM ubuntu:latest
MAINTAINER Oleh Rybalchenko 'oryba@cloudflex.team'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ['python']
CMD ['entry.py']