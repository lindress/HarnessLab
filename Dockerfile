FROM python:latest

WORKDIR /usr/local/bin

COPY Pokemon.py ./

COPY Pokemon/ ./Pokemon

CMD ["python", "Pokemon.py"]