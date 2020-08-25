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

# Comment out, use command in docker-compose
# CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "5000"]