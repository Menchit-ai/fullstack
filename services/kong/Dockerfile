FROM kong:2.6.0-ubuntu
USER root
RUN apt-get install -y git unzip

RUN apt update
RUN apt install curl
RUN curl -sL https://github.com/kong/deck/releases/download/v1.8.2/deck_1.8.2_linux_amd64.tar.gz -o deck.tar.gz
RUN tar -xf deck.tar.gz -C /tmp
RUN cp /tmp/deck /usr/local/bin/

RUN luarocks install lua-resty-session
RUN luarocks install lua-resty-openidc
RUN luarocks install kong-oidc