from django.core.management.base import BaseCommand
from staff.models import PDF, Subject, Teacher
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Create random datas'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int,
                            help='Indicates the number of datas to be created')
        parser.add_argument('data', type=str,
                            help='Indicates the type of datas to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        data = kwargs['data']
        subjects = Subject.objects.all().count()
        random_subject = Subject.objects.all(
        )[random.randint(0, subjects - 1)]
        if data == 'teachers':
            for i in range(total):
                Teacher.objects.create(
                    full_name=Faker().name(), description=Faker().text(), subject=random_subject, photo='teachers/1540580465108_rkNGJkW.jpeg')
        elif data == 'pdfs':
            for i in range(total):
                PDF.objects.create(
                    title=Faker().name(), category=random_subject, file='pdf/Tech_CV_14.pdf')
        self.stdout.write(self.style.SUCCESS(
            'Successfully created {} {}'.format(total, data)))
