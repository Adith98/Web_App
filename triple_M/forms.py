from django import forms
from django.forms import ModelForm
from .models import Personal_Detail, Exam_Record, Internship_Detail, Placement_Detail


class LoginMentee(forms.Form):
    regno = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    regno.widget.attrs['placeholder'] = "Enter Register Number"
    regno.widget.attrs['class'] = "form-control"
    regno.widget.attrs['id'] = "regno"
    regno.widget.attrs['name'] = "regno"
    password.widget.attrs['placeholder'] = "Enter password"
    password.widget.attrs['class'] = "form-control"
    password.widget.attrs['id'] = "password"
    password.widget.attrs['name'] = "password"


class LoginMentor(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    email.widget.attrs['placeholder'] = "Enter Sakec Email"
    email.widget.attrs['class'] = "form-control"
    email.widget.attrs['id'] = "email"
    email.widget.attrs['name'] = "email"
    password.widget.attrs['placeholder'] = "Enter password"
    password.widget.attrs['class'] = "form-control"
    password.widget.attrs['id'] = "password"
    password.widget.attrs['name'] = "password"


class ChangePassword(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    reenter_new_password = forms.CharField(widget=forms.PasswordInput)
    current_password.widget.attrs['placeholder'] = "Enter Current Password"
    current_password.widget.attrs['class'] = "form-control"
    current_password.widget.attrs['id'] = "current_password"
    current_password.widget.attrs['name'] = "current_password"
    new_password.widget.attrs['placeholder'] = "Enter New Password"
    new_password.widget.attrs['class'] = "form-control"
    new_password.widget.attrs['id'] = "new_password"
    new_password.widget.attrs['name'] = "new_password"
    reenter_new_password.widget.attrs['placeholder'] = "Enter Reenter New Password"
    reenter_new_password.widget.attrs['class'] = "form-control"
    reenter_new_password.widget.attrs['id'] = "reenter_new_password"
    reenter_new_password.widget.attrs['name'] = "reenter_new_password"


class SignupMentee(forms.Form):
    pass


class SignupMentor(forms.Form):
    pass


class PersonalDetailForm(ModelForm):
    class Meta:
        model = Personal_Detail
        fields = ['profile_photo', 'email', 'gender', 'dob', 'ph_no', 'parent_ph_no', 'address', 'department', 'year',
                  'division', 'current_semester', 'smart_card_number',
                  'roll_no']
        widgets = {
            'dob': forms.DateInput(format=('%m/%d/%Y'),
                                   attrs={'type': 'date'}),
        }


class ExamRecordForm(ModelForm):
    sem_1_marksheet = forms.FileField(required=False)
    sem_2_marksheet = forms.FileField(required=False)
    sem_3_marksheet = forms.FileField(required=False)
    sem_4_marksheet = forms.FileField(required=False)
    sem_5_marksheet = forms.FileField(required=False)
    sem_6_marksheet = forms.FileField(required=False)
    sem_7_marksheet = forms.FileField(required=False)
    sem_8_marksheet = forms.FileField(required=False)

    class Meta:
        model = Exam_Record
        exclude = ['admitted_student', 'year', 'verified']
        widgets = {
            'sem_1_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_2_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_3_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_4_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_5_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_6_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_7_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
            'sem_8_dop': forms.DateInput(format=('%m/%d/%Y'),
                                         attrs={'type': 'date'}),
        }


class InternshipDetailForm(ModelForm):
    class Meta:
        model = Internship_Detail
        exclude = ['admitted_student', 'verified']
        widgets = {
            'duration_start': forms.DateInput(format=('%m/%d/%Y'),
                                              attrs={'type': 'date'}),
            'duration_end': forms.DateInput(format=('%m/%d/%Y'),
                                            attrs={'type': 'date'})
        }


class PlacementDetailForm(ModelForm):
    class Meta:
        model = Placement_Detail
        exclude = ['admitted_student', 'verified']
