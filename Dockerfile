FROM ubuntu:latest
RUN apt update && apt-get -y -q install python3
RUN mkdir \usr\games\master_Mind
