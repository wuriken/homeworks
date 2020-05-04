import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate teachers with param'  # noqa builtin name from python

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=str, help='Create teachers count',)

    def handle(self, *args, **options):
        fake = Faker()
        count = 100
        if options.get('count'):
            if options.get('count').isdigit():
                count = int(options.get('count'))
        choices = ['High', 'Middle', 'Low']
        for _ in range(count):
            Teacher.objects.create(first_name=fake.first_name(),
                                   last_name=fake.last_name(),
                                   age=random.randint(22, 60),
                                   education=random.choice(choices),
                                   )
