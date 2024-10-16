FROM python:3.11-alpine

WORKDIR /app

COPY /mkdocs/ .

RUN pip install mkdocs mkdocs-swagger-ui-tag

EXPOSE 8000

CMD mkdocs serve -a 0.0.0.0:8000
