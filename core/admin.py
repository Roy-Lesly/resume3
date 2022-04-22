from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Personal, Education, ProfExperience, OtherTraining, Skills, Language, Achievement, Gallery, Hobby, Reference])