# Generated by Django 3.0.3 on 2020-05-08 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0003_internship_details_messages_placement_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Internship_Details',
            new_name='Internship_Detail',
        ),
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.RenameModel(
            old_name='Placement_Details',
            new_name='Placement_Detail',
        ),
        migrations.RemoveField(
            model_name='personal_detail',
            name='admitted_student',
        ),
        migrations.DeleteModel(
            name='Exam_Record',
        ),
        migrations.DeleteModel(
            name='Personal_Detail',
        ),
    ]
