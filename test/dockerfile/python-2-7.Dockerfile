FROM python:2.7

WORKDIR /usr/src/app
ENV PYTHONPATH=/usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . .
