FROM python:3.10-alpine

WORKDIR /home/project

COPY .env .env

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN apk add musl-locales
RUN apk add lang
ENV MUSL_LOCPATH /usr/share/i18n/locales/musl
ENV CHARSET pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LC_COLLATE pt_BR.UTF-8

CMD ["python", "main/main.py"]
