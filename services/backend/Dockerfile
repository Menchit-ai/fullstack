FROM python:3.8-buster

RUN apt update
RUN apt install curl
RUN curl -sL https://github.com/kong/deck/releases/download/v1.8.2/deck_1.8.2_linux_amd64.tar.gz -o deck.tar.gz
RUN tar -xf deck.tar.gz -C /tmp
RUN cp /tmp/deck /usr/local/bin/

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]