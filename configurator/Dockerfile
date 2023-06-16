FROM python:3.11.4-bullseye

WORKDIR /configurator
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["./start.sh"]