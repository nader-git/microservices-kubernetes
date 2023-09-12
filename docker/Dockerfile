FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip

COPY ./docker/main.py /

COPY ./docker/requirements.txt /

RUN python3 -m pip install -r requirements.txt

CMD ["uvicorn", "--host=0.0.0.0", "--port=80", "main:app"]