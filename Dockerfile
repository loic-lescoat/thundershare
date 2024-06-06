FROM python:3.12.3

WORKDIR /deploy
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY app.py .
COPY Makefile .
RUN echo hi
COPY templates/ templates/

RUN mkdir storage

RUN ls
RUN ls templates

EXPOSE 8000
CMD make run
