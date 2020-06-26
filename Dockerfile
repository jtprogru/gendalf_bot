FROM python:3.8-slim-buster

WORKDIR /botname

COPY requirements.txt /botname/
RUN pip install -r /botname/requirements.txt
COPY . /botname/

CMD python3 /botname/app.py
