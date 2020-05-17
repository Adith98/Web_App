from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.contrib.auth.hashers import make_password
from datetime import date
import os, time, random, string
from uuid import uuid4


# Create your models here.

class Mentor(models.Model):
    mentor_name = models.CharField(max_length=50)
    mentor_email = models.EmailField()
    mentor_password = models.CharField(max_length=100)
    mentor_phone_no = models.IntegerField()
    mentor_previous_batch = models.IntegerField()

    def __str__(self):
        return self.mentor_name


class Admitted_Student(models.Model):
    reg_no = models.IntegerField()
    password = models.CharField(max_length=1000000)
    first_name = models.CharField(max_length=20, default='None')
    last_name = models.CharField(max_length=20, default='None')

    def __str__(self):
        return str(self.reg_no)


class Mentor_Mentee(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    admitted_student = models.ForeignKey(Admitted_Student, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} -- {1}".format(self.mentor.mentor_name, str(self.admitted_student.reg_no))


class Personal_Detail(models.Model):
    admitted_student = models.ForeignKey(Admitted_Student, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("MALE", "MALE"), ("FEMALE", "FEMALE")), null=True, blank=True)
    dob = models.CharField(max_length=40, null=True, blank=True)
    ph_no = models.IntegerField(null=True, blank=True)
    parent_ph_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photo/", null=True, blank=True)
    department = models.CharField(max_length=10,
                                  choices=(("IT", "IT"), ("COMPS", "COMPS"), ("ETRX", "ETRX"), ("EXTC", "EXTC")),
                                  null=True, blank=True)
    year = models.CharField(max_length=2, choices=(("FE", "FE"), ("SE", "SE"), ("TE", "TE"), ("BE", "BE")),
                            null=True, blank=True)
    division = models.CharField(max_length=2,
                                choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6")),
                                null=True, blank=True)
    roll_no = models.IntegerField(null=True, blank=True)
    verified = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), default="NO")

    def __str__(self):
        return "{0} - {1} {2}".format(str(self.admitted_student.reg_no), self.admitted_student.first_name,
                                      self.admitted_student.last_name)


class Exam_Record(models.Model):
    def upload_pdf_validator(upload_pdf_obj):
        ext = os.path.splitext(upload_pdf_obj.name)[1]  # [0] = returns path+filename
        valid_extension = ['.pdf', '.PDF']
        if not ext in valid_extension:
            raise ValidationError(u'Unsupported file extension, .pdf only.')

    @deconstructible
    class Path(object):
        def __init__(self, sub_path):
            self.path = sub_path

        def __call__(self, instance, filename):
            ext = filename.split('.')[-1]
            print("path: ", self.path)
            if 'sem' in self.path.split('/')[1]:
                f_name = '{}'.format(self.path.split('/')[1])
                print("name: ", f_name)
                self.path = '{}/{}/{}'.format(self.path.split('/')[0], instance, self.path.split('/')[1])
                print("updated path: ", self.path)
            filename = '{}-marksheet_{}.{}'.format(instance, self.path.split('/')[2], ext)
            print("filename: ", filename)
            print("full path: C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                os.path.join(self.path, filename)))

            if os.path.exists(
                    "C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                        os.path.join(self.path, filename))):
                os.remove(
                    "C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                        os.path.join(self.path, filename)))

            return os.path.join(self.path, filename)

    admitted_student = models.ForeignKey(Admitted_Student, on_delete=models.CASCADE)
    year = models.CharField(max_length=2, choices=(("FE", "FE"), ("SE", "SE"), ("TE", "TE"), ("BE", "BE")))
    sem_1_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    sem_1_marksheet = models.FileField(upload_to=Path("academic_details/sem1/"),
                                       validators=[upload_pdf_validator])
    sem_1_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_1_atkt = models.IntegerField(null=True, blank=True)
    sem_1_sgpi = models.FloatField(null=True, blank=True)
    sem_1_attempts = models.IntegerField(null=True, blank=True)
    sem_2_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_2_marksheet = models.CharField(null=True,max_length=100)
    sem_2_marksheet = models.FileField(upload_to=Path("academic_details/sem2/"),
                                       validators=[upload_pdf_validator])
    sem_2_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_2_atkt = models.IntegerField(null=True, blank=True)
    sem_2_sgpi = models.FloatField(null=True, blank=True)
    sem_2_attempts = models.IntegerField(null=True, blank=True)
    sem_3_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_3_marksheet = models.CharField(null=True,max_length=100)
    sem_3_marksheet = models.FileField(upload_to=Path("academic_details/sem3/"),
                                       validators=[upload_pdf_validator])
    sem_3_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_3_atkt = models.IntegerField(null=True, blank=True)
    sem_3_sgpi = models.FloatField(null=True, blank=True)
    sem_3_attempts = models.IntegerField(null=True, blank=True)
    sem_4_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_4_marksheet = models.CharField(null=True,max_length=100)
    sem_4_marksheet = models.FileField(upload_to=Path("academic_details/sem4/"),
                                       validators=[upload_pdf_validator])
    sem_4_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_4_atkt = models.IntegerField(null=True, blank=True)
    sem_4_sgpi = models.FloatField(null=True, blank=True)
    sem_4_attempts = models.IntegerField(null=True, blank=True)
    sem_5_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_5_marksheet = models.CharField(null=True,max_length=100)
    sem_5_marksheet = models.FileField(upload_to=Path("academic_details/sem5/"),
                                       validators=[upload_pdf_validator])
    sem_5_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_5_atkt = models.IntegerField(null=True, blank=True)
    sem_5_sgpi = models.FloatField(null=True, blank=True)
    sem_5_attempts = models.IntegerField(null=True, blank=True)
    sem_6_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_6_marksheet = models.CharField(null=True,max_length=100)
    sem_6_marksheet = models.FileField(upload_to=Path("academic_details/sem6/"),
                                       validators=[upload_pdf_validator])
    sem_6_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_6_atkt = models.IntegerField(null=True, blank=True)
    sem_6_sgpi = models.FloatField(null=True, blank=True)
    sem_6_attempts = models.IntegerField(null=True, blank=True)
    sem_7_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_7_marksheet = models.CharField(null=True,max_length=100)
    sem_7_marksheet = models.FileField(upload_to=Path("academic_details/sem7/"),
                                       validators=[upload_pdf_validator])
    sem_7_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_7_atkt = models.IntegerField(null=True, blank=True)
    sem_7_sgpi = models.FloatField(null=True, blank=True)
    sem_7_attempts = models.IntegerField(null=True, blank=True)
    sem_8_cleared = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), null=True, blank=True)
    # sem_8_marksheet = models.CharField(null=True,max_length=100)
    sem_8_marksheet = models.FileField(upload_to=Path("academic_details/sem8/"),
                                       validators=[upload_pdf_validator])
    sem_8_dop = models.CharField(max_length=40, null=True, blank=True)
    sem_8_atkt = models.IntegerField(null=True, blank=True)
    sem_8_sgpi = models.FloatField(null=True, blank=True)
    sem_8_attempts = models.IntegerField(null=True, blank=True)
    verified = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), default="NO")

    def __str__(self):
        return str(self.admitted_student.reg_no)


class Internship_Detail(models.Model):
    admitted_student = models.ForeignKey(Admitted_Student, on_delete=models.CASCADE)
    company = models.CharField(max_length=40)
    position = models.CharField(max_length=100)
    duration_start = models.CharField(max_length=40)
    duration_end = models.CharField(max_length=40)

    def upload_pdf_validator(upload_pdf_obj):
        ext = os.path.splitext(upload_pdf_obj.name)[1]  # [0] = returns path+filename
        valid_extension = ['.pdf', '.PDF']
        if not ext in valid_extension:
            raise ValidationError(u'Unsupported file extension, .pdf only.')

    @deconstructible
    class PathAndRename(object):
        def __init__(self, sub_path):
            self.path = sub_path

        def __call__(self, instance, filename):
            ext = filename.split('.')[-1]
            print(self.path)
            f_name = 'internship_{}'.format(self.path.split('/')[1])
            filename = '{}-{}-{}.{}'.format(instance, instance.company, f_name, ext)
            print(os.path.join(self.path, filename))
            if os.path.exists(
                    "C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                        os.path.join(self.path, filename))):
                os.remove(
                    "C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                        os.path.join(self.path, filename)))

            return os.path.join(self.path, filename)

    certificate = models.FileField(upload_to=PathAndRename("internship_details/certificate/"),
                                   validators=[upload_pdf_validator])
    intern_eval = models.FileField(upload_to=PathAndRename("internship_details/intern_eval/"),
                                   validators=[upload_pdf_validator])
    verified = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), default="NO")

    def __str__(self):
        return str(self.admitted_student.reg_no)


class Placement_Detail(models.Model):
    admitted_student = models.ForeignKey(Admitted_Student, on_delete=models.CASCADE)
    company = models.CharField(max_length=40)
    position = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    bond = models.CharField(max_length=100)
    ctc = models.CharField(max_length=100)
    hr_email = models.EmailField()
    placed_through = models.CharField(max_length=100)

    def upload_pdf_validator(upload_pdf_obj):
        ext = os.path.splitext(upload_pdf_obj.name)[1]
        # [0] = returns path+filename
        valid_extension = ['.pdf', '.PDF']
        if not ext in valid_extension:
            raise ValidationError(u'Unsupported file extension, .pdf only.')

    @deconstructible
    class PathAndRename(object):
        def __init__(self, sub_path):
            self.path = sub_path

        def __call__(self, instance, filename):
            ext = filename.split('.')[-1]
            print(self.path)
            f_name = 'placement_{}'.format(self.path.split('/')[1])
            filename = '{}-{}-{}.{}'.format(instance, instance.company, f_name, ext)
            print(os.path.join(self.path, filename))
            if os.path.exists(
                    "C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                        os.path.join(self.path, filename))):
                os.remove(
                    "C:/Users/shetty/Desktop/adith/SAKEC/Sakec_Internship/Web_App/media/{}".format(
                        os.path.join(self.path, filename)))

            return os.path.join(self.path, filename)

    offer_letter = models.FileField(upload_to=PathAndRename("placement_details/offer_letter/"),
                                    validators=[upload_pdf_validator])
    details = models.CharField(max_length=10000)
    verified = models.CharField(max_length=3, choices=(("YES", "YES"), ("NO", "NO")), default="NO")

    def __str__(self):
        return str(self.admitted_student.reg_no)


class Message(models.Model):
    admitted_student = models.ForeignKey(Admitted_Student, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=(
        ("Personal Details", "Personal Details"), ("Exam Details", "Exam Details"),
        ("Internship Details", "Internship Details"), ("Placement Details", "Placement Details"), ("Other", "Other")))
    message = models.CharField(max_length=10000)
    datetime = models.DateTimeField()

    def __str__(self):
        return "{0} - {1}".format(str(self.admitted_student.reg_no), self.category)
