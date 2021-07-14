from rest_framework import viewsets, permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer

from library.serializer import *
from rest_framework.filters import SearchFilter
from knox.models import AuthToken
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ('username',)


class SemesterViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    filter_backends = [SearchFilter]
    search_fields = ('semester',)


class NoteViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['program_name__program_name', 'semester__semester',]



class ProgramViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_backends = [SearchFilter]
    search_fields = ('program_name', 'semester__semester')


class SyllabusViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    filter_backends = [SearchFilter]
    search_fields = ('program_name__program_name', 'semester__semester')


class PaperViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = OldQuestionPaper.objects.all()
    serializer_class = OldQuestionPaperSerializer
    filter_backends = [SearchFilter]
    search_fields = (
        'added_by', 'date_of_added', 'date_of_modified', 'program_name__program_name', 'semester__semester')


class SubjectViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    filter_backends = [SearchFilter]
    search_fields = ('subject_name', 'program_name__program_name', 'semester__semester')


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)