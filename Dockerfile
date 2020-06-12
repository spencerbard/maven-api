FROM python:3.8

LABEL maintainer="sbard26@gmail.com"

WORKDIR /maven

COPY api/requirements.txt api/requirements.txt

RUN pip install -r api/requirements.txt

COPY api api

ENTRYPOINT [ "gunicorn" ]
CMD [ "--bind", "0.0.0.0:5000", "api.wsgi:app" ]