# Generated by Django 3.0.3 on 2020-05-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0016_auto_20200516_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship_detail',
            name='certificate',
            field=models.FileField(upload_to='internship_files/pdfs/'),
        ),
    ]
