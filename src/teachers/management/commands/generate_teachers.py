import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate teachers with param'  # noqa builtin name from python

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=str, help='Create teachers count',)  # noqa

    def handle(self, *args, **options):
        fake = Faker()
        count = 100
        if options.get('count'):
            if options.get('count').isdigit():
                count = int(options.get('count'))
        choices = ['High', 'Middle', 'Low']
        insert_data = []
        for _ in range(count):
            insert_data.append(Teacher(first_name=fake.first_name(),
                                       last_name=fake.last_name(),
                                       age=random.randint(22, 60),
                                       education=random.choice(choices),
                                       ))
        Teacher.objects.bulk_create(insert_data)
