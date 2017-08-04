FROM ubuntu:14.04
MAINTAINER Srihari Rao <harirao3@gmail.com>

RUN apt-get -qq update && apt-get install -y
RUN	apt-get -qq -y install python3

RUN apt-get -qq -y install python3-pip
RUN	pip3 install nltk

ENV CORPORA book

RUN python3 -m nltk.downloader $CORPORA

EXPOSE 9000
ADD ./ /nltkServer
WORKDIR /nltkServer

CMD ["python3","nltkServer.py"]
