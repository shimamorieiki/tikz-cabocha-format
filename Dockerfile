FROM python:latest

RUN apt-get update && apt-get upgrade -y

WORKDIR /root

# ユーザーを作成
ARG UID=1000
RUN useradd -m -u ${UID} docker

# フォルダを作る
RUN mkdir -p /code
RUN chown docker /code

# 作成したユーザーに切り替える
USER ${UID}

WORKDIR /code
ADD requirements.txt /code/

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

ADD . /code/

USER root
RUN chown -hR docker:docker /code

USER ${UID}
CMD /bin/bash