import os
import django
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE","onlineproject.settings")
django.setup()
from onlineapp.models import *
def insert_into_techer_model():
    c = Teacher(name="teacher1",email="test1@gmail.com",college=college.objects.get(id=239))
    c.save()
def perform_query():
    c = college.objects.values("name").filter(acronym='anits').annotate(teacher_count=Count("teacher"), student_count=Count("student"))
    #it is bug in django
    for row in list(c):
        print(row)
#insert_into_techer_model()
perform_query()