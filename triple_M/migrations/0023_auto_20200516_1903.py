# Generated by Django 3.0.3 on 2020-05-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0022_auto_20200516_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_record',
            name='sem_1_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_2_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_3_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_4_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_5_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_6_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_7_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='exam_record',
            name='sem_8_marksheet',
            field=models.CharField(max_length=100, null=True),
        ),
    ]