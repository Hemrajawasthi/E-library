from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from library.models import Semester, Program, Note, OldQuestionPaper, Syllabus, Subject


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
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    program_name = serializers.StringRelatedField(read_only=True)
    semester = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subject
        # fields = ['id','program_name','semester','subject_name', 'subject_code','credit_hrs']
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):

    semester = serializers.StringRelatedField(read_only=True)
    program_name = serializers.StringRelatedField(read_only=True)
    subject = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'


class OldQuestionPaperSerializer(serializers.ModelSerializer):
    semester = serializers.StringRelatedField(read_only=True)
    program_name = serializers.StringRelatedField(read_only=True)
    subject = serializers.StringRelatedField(read_only=True)
    subject_code = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OldQuestionPaper
        fields = '__all__'


class SyllabusSerializer(serializers.ModelSerializer):

    semester = serializers.StringRelatedField(read_only=True)
    program_name = serializers.StringRelatedField(read_only=True)
    subject = serializers.StringRelatedField(read_only=True)
    subject_code = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Syllabus
        fields = '__all__'
