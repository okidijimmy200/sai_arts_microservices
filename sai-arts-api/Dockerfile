FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

EXPOSE 8000

# ENTRYPOINT ["python", "./app/manage.py", "runserver", "0.0.0.0:8000" ]
CMD ["sh","-c","export DJANGO_SETTINGS_MODULE=app.settings.pro && python ./app/manage.py migrate && python ./app/manage.py initadmin && python ./app/manage.py runserver 0.0.0.0:8000"]