FROM python:3.12.3

WORKDIR /deploy
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

ARG PORT
ENV PORT=${PORT}

COPY app.py .
COPY Makefile .
COPY templates/ templates/

ENV STORAGE_DIR=storage

RUN mkdir $STORAGE_DIR

EXPOSE $PORT
CMD flask --app app run -h 0.0.0.0 -p $PORT
