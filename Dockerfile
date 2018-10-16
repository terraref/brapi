FROM python:3-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

#RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "bety_brapi"]
