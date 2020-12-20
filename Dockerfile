FROM python:3

RUN apt-get update -y && apt-get install -y mariadb-server

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ./start.sh
