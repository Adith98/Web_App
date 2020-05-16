# Generated by Django 3.0.3 on 2020-05-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0007_auto_20200510_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_record',
            name='year',
            field=models.CharField(choices=[('FE', 'FE'), ('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE')], default=None, max_length=2),
            preserve_default=False,
        ),
    ]
