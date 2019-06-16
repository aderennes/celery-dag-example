FROM python:3.7.2

RUN mkdir /app/
WORKDIR /app/

ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD dag/ /app/dag/
WORKDIR /app/dag/

ENTRYPOINT celery -A tasks worker --loglevel=info