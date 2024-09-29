import os

from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create superuser if not exist'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
            else:
                self.stdout.write(self.style.WARNING('Superuser already exists.'))
        else:
            self.stdout.write(self.style.ERROR('Please provide both username and email and password.'))