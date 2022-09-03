from faker import Faker
from my_app.models import AccessRecord, Webpage, Topic
import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULES', 'my_app.settings')

django.setup()
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range:
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        