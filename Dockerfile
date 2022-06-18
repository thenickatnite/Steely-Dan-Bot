FROM python:3.10.5-slim-buster

COPY bot /bot
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "main.py"]