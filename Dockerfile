FROM python:3.10-slim

RUN apt-get update && apt-get install -y calibre wget curl

WORKDIR /app

COPY recipes/ ./recipes/
COPY download_and_send.py .

ENV ORBYT_USER=''
ENV ORBYT_PASS=''
ENV FROM_EMAIL=''
ENV APP_PASSWORD=''
ENV TO_EMAIL=''

CMD ["python", "download_and_send.py"]
