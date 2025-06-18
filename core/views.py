
from rest_framework import generics, permissions, filters
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Patient, Doctor, PatientDoctor
from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    PatientDoctorSerializer,
)


class IsOwner(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


#  PATIENTS 
class PatientListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = PatientSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)


#  DOCTORS 
class DoctorListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-created_at"]

    def get_queryset(self):
       
        return Doctor.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = DoctorSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Doctor.objects.filter(created_by=self.request.user)


#  PATIENT DOCTOR MAPPINGS
class MappingListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientDoctorSerializer

    def get_queryset(self):
        
        return PatientDoctor.objects.filter(patient__created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save() 


class MappingByPatient(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = PatientDoctorSerializer

    def get_queryset(self):
        return PatientDoctor.objects.filter(
            patient_id=self.kwargs["patient_id"],
            patient__created_by=self.request.user,
        )


class MappingDetail(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientDoctorSerializer

    def get_queryset(self):
        return PatientDoctor.objects.filter(patient__created_by=self.request.user)
