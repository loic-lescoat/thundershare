FROM python:3.12.3

WORKDIR /deploy
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY app.py .
COPY constants.py .
COPY Makefile .
COPY favicon.ico .
COPY templates/ templates/
COPY src/ src/

ENV STORAGE_DIR=storage

ARG PORT
ENV PORT=${PORT}
EXPOSE $PORT

CMD gunicorn -w 1 app:app -b thundershare:$PORT
