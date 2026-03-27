FROM python:3.13-slim
RUN apt-get update && apt-get install -y get
WORKDIR /app
RUN git clone https://github.com/Nawit-dev/HomeWork3.git .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","-m","pytest", "-s", "tests"]
VOLUME ["/app/logs"]