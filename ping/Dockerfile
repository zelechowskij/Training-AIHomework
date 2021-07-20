FROM python:3.8-slim

WORKDIR /ping

ENV FLASK_APP=ping.py
ENV FLASK_RUN_HOST=0.0.0.0 
RUN apt-get update && apt-get install curl -y
COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["flask", "run", "-p", "8080"]