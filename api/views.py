from rest_framework import viewsets, generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from courses.models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer