FROM python:latest

WORKDIR /usr/local/bin

COPY hello.py ./

CMD ["python", "./hello.py"]