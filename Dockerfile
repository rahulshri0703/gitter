FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "gunicorn" ]
CMD [ "--bind=0.0.0.0:5000","app:app" ]