# FROM tensorflow/tensorflow:1.15.0-py3
FROM python:3.7-buster

ENV LANG=C.UTF-8
RUN mkdir /gpt-2
WORKDIR /gpt-2
ADD . /gpt-2
RUN pip3 install -r requirements.txt
RUN python3 download_model.py 124M

CMD python3 auto_generate_texts.py