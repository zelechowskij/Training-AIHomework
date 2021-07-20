FROM python:3.8-slim

WORKDIR /info

ENV FLASK_APP=info.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["flask", "run", "-p", "8080"]