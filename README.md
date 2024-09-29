# Web Development Assignment 1

> This project just for demonstrating how to use Django with templates.

## prediction

1. Linux or Mac
2. Installed python 3.12(this project just tested at this version)

## Prepare virtual environment

active venv
```shell
cd [the root of this project]
python3 -m venv .venv
source venv/bin/activate
```

exit venv
```shell
deactivate
```

## Install dependencies

```shell
pip install requirements.txt
```

## Set environment variables

This information recorded by .env and Dockerfile
```shell
export DJANGO_DEBUG=False
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@django-example.app
```

Can use next command to add environment stored in .env file
```shell
source .env
```

Check them like this
```shell
echo $DJANGO_SUPERUSER_USERNAME
```

## Init data
```shell
# create tables
python manage.py migrate

# create super user
# option 1: by interactive way
python manage.py createsuperuser

# option 2: by environment variables
python manage.py create_superuser
```

## Run server

```shell
python3 manage.py runserver
```

## Docker deploy

```shell
# build local image
sudo docker build -t [your image tag name for this project] .

# Run 
sudo docker run -p 8000:8000 [image tag name]

# Run the container in detached mode.
sudo docker run -d --name [container name] -p 8000:8000 [image tag name]
sudo docker start [container name]
sudo docker stop [container name]
```




