FROM alpine:edge
MAINTAINER Dominique DERRIER derrierdo@gmail.com
RUN apk add --update py2-pip && pip install docker-py && echo "cd www ;python -m CGIHTTPServer 8000 /www" > Start.sh && chmod a+x Start.sh
ADD html /www
EXPOSE 8000:8000
ENTRYPOINT /Start.sh
