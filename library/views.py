from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser

from .serializer import UserSerializer
from library.models import Semester, Note, Program, Syllabus
from library.serializer import *
# from library.serializer import SemesterSerializer, NoteSerializer, ProgramSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_notes(request):

    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def api_program(request):
    if request.method == 'GET':
        program = Program.objects.all()
        serializer = ProgramSerializer(program, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProgramSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def api_semester(request):
    if request.method == 'GET':
        semester = Semester.objects.all()
        serializer = SemesterSerializer(semester, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SemesterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def api_users(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def api_oldquestionpaper(request):
    if request.method == 'GET':
        old = OldQuestionPaper.objects.all()
        serializer = OldQuestionPaperSerializer(old, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SemesterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def api_syllabus(request):

    if request.method == 'GET':
        syllabus = Syllabus.objects.all()
        serializer = SyllabusSerializer(syllabus, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SyllabusSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#
# class SemesterViewSet(viewsets.ModelViewSet):
#     queryset = Semester.objects.all()
#     serializer_class = SemesterSerializer
#
#
# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#
# class ProgramViewSet(viewsets.ModelViewSet):
#     queryset = Program.objects.all()
#     serializer_class = ProgramSerializer


#
# @csrf_exempt
# @api_view(['GET','PUT', 'POST','DELETE'])
# @permission_classes([IsAuthenticated])
#
# def api_notess(request, id):
#     try:
#         name = Note.objects.get(id=id)
#     except Note.DoesNotExists:
#         return HttpResponse(status= 404)
#
#     if request.method == 'GET':
#         data_res= NoteSerializer(Note)
#         return JsonResponse(data_res.data)

