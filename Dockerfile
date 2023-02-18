FROM python:3.9

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y gettext libgettextpo-dev

COPY ./requirements.txt /requirements.txt
COPY ./.env.dev /.env.dev
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade -r /requirements.txt
RUN apt-get install sqlite3

ADD . /bot
WORKDIR /bot

ENTRYPOINT ["python", "server.py"]