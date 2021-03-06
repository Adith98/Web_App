# Generated by Django 3.0.3 on 2020-05-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0026_auto_20200516_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_detail',
            name='current_semester',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='personal_detail',
            name='smart_card_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='mentor_password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personal_detail',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/'),
        ),
    ]
