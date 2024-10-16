FROM ubuntu:22.04

RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD cd ./src && python3 webapp.py
