from rest_framework import viewsets, permissions
from library.serializer import *
from rest_framework.filters import SearchFilter


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ('username',)


class SemesterViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    filter_backends = [SearchFilter]
    search_fields = ('semester',)


class NoteViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


    # criterion1 = Note(program_name__program_name="bca")
    # criterion2 = Note(semester__semester="first semester")
    # Note = Note.objects.filter('program_name__program_name' & 'semester__semester')

    filter_backends = [SearchFilter]
    search_fields = (
        'subject__subject_name', 'program_name__program_name', 'semester__semester', 'added_by', 'date_of_added',
        'date_of_modified')


class ProgramViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_backends = [SearchFilter]
    search_fields = ('program_name', 'semester__semester')


class SyllabusViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    filter_backends = [SearchFilter]
    search_fields = ('program_name__program_name', 'semester__semester')


class PaperViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = OldQuestionPaper.objects.all()
    serializer_class = OldQuestionPaperSerializer
    filter_backends = [SearchFilter]
    search_fields = (
        'added_by', 'date_of_added', 'date_of_modified', 'program_name__program_name', 'semester__semester')


class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    filter_backends = [SearchFilter]
    search_fields = ('subject_name', 'program_name__program_name', 'semester__semester')
