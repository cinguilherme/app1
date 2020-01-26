FROM python:3.7

COPY . app/

RUN pip install --upgrade pip

RUN pip install -r app/requirements.txt

EXPOSE 5000