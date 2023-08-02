# python base image in the container from Docker Hub
FROM python:3.7

# copy files to the /app folder in the container
COPY app.py /app/app.py
COPY utils /app/utils
COPY train/models /app/train/models
COPY requirements.txt /app/requirements.txt
COPY gunicorn.conf.py /app/gunicorn.conf.py

# set the working directory in the container to be /app
WORKDIR /app

RUN mkdir -p /app/logs

# install the packages from the Pipfile in the container
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# expose the port that uvicorn will run the app on
ENV PORT=80

EXPOSE 80

CMD ["gunicorn", "app:server"]
