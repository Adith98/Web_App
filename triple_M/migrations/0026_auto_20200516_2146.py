# Generated by Django 3.0.3 on 2020-05-16 16:16

from django.db import migrations, models
import triple_M.models


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0025_auto_20200516_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_record',
            name='sem_1_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_2_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_3_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_4_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_5_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_6_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_7_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_8_marksheet',
            field=models.FileField(upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='personal_detail',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='profile_photo/'),
        ),
    ]
