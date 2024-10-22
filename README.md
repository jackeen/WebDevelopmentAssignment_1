# Web Development Assignment 1

> This project just for demonstrating how to use Django with templates.
> The style of this project is built by Bootstrap.

## Prediction

1. Linux or Mac
2. Installed python 3.12(this project just tested at this version)

## Allowed hosts

```python
# The default allowed demain list at setting.py
ALLOWED_HOSTS = ['*']
```

## Deploy local

### Prepare virtual environment

```shell
# active venv
cd [the root of this project]
python3 -m venv .venv
source venv/bin/activate
```

```shell
# exit venv
deactivate
```

### Install dependencies

```shell
pip install -r requirements.txt
```

### Set environment variables

```shell
# This information recorded by .env and Dockerfile
export DJANGO_DEBUG=False
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@django-example.app
```

```shell
# add environment stored in .env file
source .env
```

```shell
# Check environment
echo $DJANGO_SUPERUSER_USERNAME
```

### Init data
```shell
# create tables
python manage.py migrate

# create super user
# option 1: by interactive way
python manage.py createsuperuser

# option 2: by environment variables based on environment setting
python manage.py create_superuser
```

### Run server

```shell
python3 manage.py runserver
```

## Docker deploy

> The docker based platforms don't need to do this, they will use Dockerfile to build then deploy.
> These commands are for local test and IssS server deploy.

```shell
# build local image
sudo docker build -t [your image tag name for this project] .

# Run 
sudo docker run -p 8000:8000 [image tag name]

# Run the container in detached mode.
sudo docker run -d --name [container name] -p 8000:8000 [image tag name]
# start container
sudo docker start [container name]
# stop container
sudo docker stop [container name]
```




