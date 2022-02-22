FROM python:3.10.2-alpine
COPY ./application /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies for sql alchemy
RUN \
 apk add --no-cache bash && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

# install required modules
RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["/bin/bash", "entrypoint.sh"]