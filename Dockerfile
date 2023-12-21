# para desenvolvimento use o Dockerfile-dev
FROM --platform=linux/amd64 python:3.10-alpine AS buid

WORKDIR /home/project

# Esta linha não é necessária para a release
#COPY .env .env

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /temp && \ cp -r assets /temp

COPY . .

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN apk add musl-locales
RUN apk add lang
ENV MUSL_LOCPATH /usr/share/i18n/locales/musl
ENV CHARSET pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LC_COLLATE pt_BR.UTF-8

RUN echo "0 12 * * * cd /home/project && /usr/local/bin/python3 /home/project/src/Main.py" >> /var/spool/cron/crontabs/root
RUN echo "0 16-22/2 * * * cd /home/project && /usr/local/bin/python3 /home/project/src/Main.py" >> /var/spool/cron/crontabs/root

CMD crond -f

ENTRYPOINT ["/home/project/scripts/docker-entrypoint.sh"]