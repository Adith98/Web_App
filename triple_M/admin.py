from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Mentor)

admin.site.register(models.Admitted_Student)

admin.site.register(models.Personal_Detail)

admin.site.register(models.Exam_Record)

admin.site.register(models.Internship_Detail)
admin.site.register(models.Placement_Detail)
admin.site.register(models.Message)

admin.site.register(models.Mentor_Mentee)


