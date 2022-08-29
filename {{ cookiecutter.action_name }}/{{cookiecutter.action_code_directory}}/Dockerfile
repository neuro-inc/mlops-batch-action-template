FROM python:3.9.12

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# SSH
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
RUN apt-get install -y tzdata

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
