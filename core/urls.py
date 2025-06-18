from django.urls import path
from . import views

urlpatterns = [
    # Patients
    path('patients/', views.PatientListCreate.as_view()),
    path('patients/<int:pk>/', views.PatientDetail.as_view()),

    # Doctors
    path('doctors/', views.DoctorListCreate.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view()),

    # Mappings
    path('mappings/', views.MappingListCreate.as_view()),
    path('mappings/<int:patient_id>/', views.MappingByPatient.as_view()),
    path('mappings/detail/<int:pk>/', views.MappingDetail.as_view()),
]
