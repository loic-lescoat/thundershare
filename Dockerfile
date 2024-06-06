FROM python:3.12.3

WORKDIR /deploy
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY app.py .
COPY Makefile .
COPY templates/ templates/

RUN mkdir storage

EXPOSE 8000
CMD flask --app app run -h 0.0.0.0 -p 8000
