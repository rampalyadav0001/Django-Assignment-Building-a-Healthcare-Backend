from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        read_only_fields = ('id', 'created_by', 'created_at')
        fields = read_only_fields + ('name', 'age', 'notes')

    def create(self, validated):
        validated['created_by'] = self.context['request'].user
        return super().create(validated)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        read_only_fields = ('id', 'created_by', 'created_at')
        fields = read_only_fields + ('name', 'speciality')

    def create(self, validated):
        validated['created_by'] = self.context['request'].user
        return super().create(validated)


class PatientDoctorSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = PatientDoctor
        fields = ('id', 'patient', 'doctor', 'assigned_at')
        read_only_fields = ('id', 'assigned_at')
