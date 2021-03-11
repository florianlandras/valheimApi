# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 80:5000

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /valheimApi/requirements.txt

WORKDIR /valheimApi

RUN pip install -r requirements.txt

COPY . /valheimApi

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]