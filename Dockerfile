FROM python:3.13-slim
RUN apt-get update && apt-get install -y get
WORKDIR /app
