FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3 \
    python3-pip \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && pip3 install redis psycopg2

COPY sender.py /app/sender.py
COPY reader.py /app/reader.py

WORKDIR /app
