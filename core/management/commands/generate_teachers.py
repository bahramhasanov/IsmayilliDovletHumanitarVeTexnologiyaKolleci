from django.core.management.base import BaseCommand
from staff.models import Subject, Teacher
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int,
                            help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        subjects = Subject.objects.all().count()
        random_subject = Subject.objects.all()[random.randint(0, subjects - 1)]
        for i in range(total):
            Teacher.objects.create(
                full_name=Faker().name(), description=Faker().text(), subject=random_subject, photo='teachers/1540580465108_rkNGJkW.jpeg')
        self.stdout.write(self.style.SUCCESS('Successfully created {} users'.format(total)))
