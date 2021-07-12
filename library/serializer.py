from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from library.models import Semester, Program, Note


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="Library:user-detail")

    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'semester']


class ProgramSerializer(serializers.ModelSerializer):
    semester = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ['id', 'program_name', 'semester']


class NoteSerializer(serializers.ModelSerializer):

    semester = serializers.StringRelatedField(read_only=True)
    program_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'


# class NoteSerializer(serializers.ModelSerializer):
#     semester = serializers.StringRelatedField(read_only=True)
#     program_name = serializers.StringRelatedField(read_only=True)
#
#     class Meta:
#         model = Note
#         fields = ['id', 'name', 'semester', 'program_name', 'added_by', 'date_of_added', 'date_of_modified']
