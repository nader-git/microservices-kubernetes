FROM ubuntu:20.04

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Retry apt-get update and install if they fail
RUN for i in {1..5}; do apt-get update && apt-get install -y python3 python3-pip --no-install-recommends && break || sleep 15; done \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

COPY ./main.py /
COPY ./requirements.txt /
RUN python3 -m pip install -r requirements.txt

CMD ["uvicorn", "--host=0.0.0.0", "--port=80", "main:app"]
