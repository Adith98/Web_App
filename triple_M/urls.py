from django.urls import path
from . import views

app_name = 'triple_M'
login_type = None
urlpatterns = [
    path('', views.LoginPage.as_view(), name='login'),
    path('<login_type>/', views.LoginTypePage.as_view(), name='login_type'),
    path('change_password', views.change_password, name='change-password'),
    path('mentor/mentor-dash', views.MentorDash.as_view(), name='mentor-dash'),
    path('mentor/contact-mentee', views.ContactMentee.as_view(), name='contact-mentee'),
    path('mentor/contact-mentee/<reg_no>', views.ContactSpecificMentee.as_view(), name='contact-mentee'),
    path('mentor/get_internship_details', views.GetInternship.as_view(), name='get-internship'),
    path('mentor/get_placement_details', views.GetPlacement.as_view(), name='get-placement'),
    path('mentor/get_details/export/<section>', views.export_csv, name='export'),
    path('mentor/verify-details', views.VerifyDetails.as_view(), name='verify-details'),
    path('mentor/verify-details/<reg_no>', views.MentorStudent.as_view(), name='mentor-student'),
    path('mentor/verify-details/<reg_no>/<section>', views.VerifySpecificCategory.as_view(), name='mentor-student'),
    path('mentor/verify-details/<reg_no>/<section>/<output>/<id>', views.ApproveOrDisapprove.as_view(),
         name='decision'),
    path('mentee/mentee-dash', views.MenteeDash.as_view(), name='mentee-dash'),
    path('mentee/contact-mentor', views.ContactMentor.as_view(), name='contact-mentor'),
    path('mentee/edit-details/<section>', views.EditDetails.as_view(), name='edit-details'),
    path('mentee/edit-details/<section>/<id>', views.EditInternship.as_view(), name='edit-details'),
    path('mentee/personal-details', views.PersonalDetails.as_view(), name='personal-details'),
    path('mentee/academic-details', views.AcademicDetails.as_view(), name='academic-details'),
    path('mentee/internship-details', views.InternshipDetails.as_view(), name='internship-details'),
    path('mentee/placement-details', views.PlacementDetails.as_view(), name='placement-details'),
    path('logout', views.logout, name='logout')
]
