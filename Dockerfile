FROM python:3.7-alpine
MAINTAINER pogremix <pogremix@yandex.ru>

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /mailer

WORKDIR /mailer
ENTRYPOINT ["python", "main.py"]
