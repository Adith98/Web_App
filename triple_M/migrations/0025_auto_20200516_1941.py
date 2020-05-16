# Generated by Django 3.0.3 on 2020-05-16 14:11

from django.db import migrations, models
import triple_M.models


class Migration(migrations.Migration):

    dependencies = [
        ('triple_M', '0024_auto_20200516_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_record',
            name='sem_1_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_2_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_3_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_4_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_5_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_6_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_7_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='exam_record',
            name='sem_8_marksheet',
            field=models.FileField(blank=True, upload_to='', validators=[triple_M.models.Exam_Record.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='internship_detail',
            name='certificate',
            field=models.FileField(upload_to='', validators=[triple_M.models.Internship_Detail.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='internship_detail',
            name='intern_eval',
            field=models.FileField(upload_to='', validators=[triple_M.models.Internship_Detail.upload_pdf_validator]),
        ),
        migrations.AlterField(
            model_name='placement_detail',
            name='offer_letter',
            field=models.FileField(upload_to='', validators=[triple_M.models.Placement_Detail.upload_pdf_validator]),
        ),
    ]
