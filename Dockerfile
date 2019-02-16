FROM python:3.6-alpine

MAINTAINER Juan Carlos Serrano Pérez <juan.carlos.wow.95@gmail.com>

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "src/app.py"]
