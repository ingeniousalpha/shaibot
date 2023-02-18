FROM python:3.9

ENV BOT_API_KEY="5870268600:AAHXqd1jRBllUWqHH1RA0wB5kZwPcm6hUNY"
ENV OPENAI_API_KEY="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"

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y gettext libgettextpo-dev

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade -r /requirements.txt
RUN apt-get install sqlite3

ADD . /bot
WORKDIR /bot

ENTRYPOINT ["python", "server.py"]