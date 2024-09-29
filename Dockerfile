# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables
ENV DJANGO_DEBUG False
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_EMAIL admin@django-example.app

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . /app/

# Init database and create superuser
RUN python3 manage.py migrate
RUN python3 manage.py create_superuser

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "WebDevelopmentAssignment_1.wsgi:application"]
