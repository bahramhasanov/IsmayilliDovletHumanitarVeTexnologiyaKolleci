from django.core.management.base import BaseCommand
from core.models import Mostquestions
from about.models import Category, Event, Faculty, News, Specialty
from staff.models import PDF, Subject, Teacher
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Create random datas'

    def add_arguments(self, parser):
        parser.add_argument('data', type=str,
                            help='Indicates the type of datas to be created')
        parser.add_argument('total', type=int,
                            help='Indicates the number of datas to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        data = kwargs['data']
        if data == 'teachers':
            subjects = Subject.objects.all().count()
            for i in range(total):
                random_subject = Subject.objects.all(
                )[random.randint(0, subjects - 1)]
                Teacher.objects.create(
                    full_name_az=Faker('tr_TR').name(), full_name_ru=Faker('ru_RU').name(),  description=Faker().text(), subject=random_subject, photo='teachers/1491483227_5914040.jpeg')
        elif data == 'pdfs':
            subjects = Subject.objects.all().count()
            for i in range(total):
                random_subject = Subject.objects.all(
                )[random.randint(0, subjects - 1)]
                PDF.objects.create(
                    title_az=Faker('tr_TR').name(), title_ru=Faker('ru_RU').name(), category=random_subject, file='pdf/Profile.pdf')
        elif data == 'news':
            categories = Category.objects.all().count()
            for i in range(total):
                random_categories = Category.objects.all(
                )[random.randint(0, categories - 1)]
                News.objects.create(
                    title=Faker().name(), description=Faker().text(), category=random_categories, image='news/1491483227_5914040.jpg')
        elif data == 'events':
            categories = Category.objects.all().count()
            for i in range(total):
                random_categories = Category.objects.all(
                )[random.randint(0, categories - 1)]
                Event.objects.create(
                    title=Faker().name(), description=Faker().text(), category=random_categories, image='event/1491483227_5914040.jpg', date=Faker().date())
        elif data == 'faculties':
            for i in range(total):
                Faculty.objects.create(
                    title=Faker().name(), description=Faker().text(), image='faculty/riyaz_VihCBZ5.png')
        elif data == 'specialities':
            categories = Faculty.objects.all().count()
            for i in range(total):
                random_faculties = Faculty.objects.all(
                )[random.randint(0, categories - 1)]
                Specialty.objects.create(
                    title=Faker().name(), description=Faker().text(), faculty=random_faculties, image_icon='specialty/1491483227_5914040.png')
        elif data == 'mostquestions':
            for i in range(total):
                Mostquestions.objects.create(
                    title=Faker().name(), description=Faker().text(),)
        self.stdout.write(self.style.SUCCESS(
            'Successfully created {} {}'.format(total, data)))
