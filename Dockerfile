FROM python:latest

WORKDIR /usr/local/bin

COPY hello.py ./

CMD ["./hello.py"]