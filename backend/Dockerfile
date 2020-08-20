# FROM python:3.8.1-slim-buster

# ENV WORKDIR=/usr/src/app
# ENV USER=app
# ENV APP_HOME=/home/app/server
# ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# WORKDIR $WORKDIR

# RUN pip install --upgrade pip
# COPY ./src/requirements.txt $WORKDIR/requirements.txt
# RUN pip install -r requirements.txt

# RUN adduser --system --group $USER
# RUN mkdir $APP_HOME
# WORKDIR $APP_HOME

# COPY . $APP_HOME
# RUN chown -R $USER:$USER $APP_HOME
# USER $USER

# Pull official base FastAPI Python image.
# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
FROM python:3.8-slim-buster

ENV WORKDIR=/usr/src/app
# Don't write .pyc and dump logs to std stream in real time.
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Set work directory path
WORKDIR $WORKDIR

# Add and install requirements
RUN pip install --upgrade pip
COPY ./src/requirements.txt $WORKDIR/requirements.txt
RUN pip install -r requirements.txt

# Add app
COPY . $WORKDIR/