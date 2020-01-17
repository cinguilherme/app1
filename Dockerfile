FROM python:3.5

COPY . app/

RUN pip install -r app/requirements.txt

EXPOSE 5000