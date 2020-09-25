FROM ubuntu:16.04
MAINTAINER Raj.Burnwal
RUN apt-get update -y \
&& apt-get install telnet curl ffmpeg -y
CMD "/bin/bash"