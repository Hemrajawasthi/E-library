from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework import routers
from knox import views as knox_views

from library import views
from library.views import *



# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet, basename='users')
router.register(r'api/semesters', SemesterViewSet, basename='semester')
router.register(r'api/notes', NoteViewSet, basename='note')
router.register(r'api/programs', ProgramViewSet, basename='program')
router.register(r'api/syllabus', SyllabusViewSet, basename='syllabus')
router.register(r'api/papers', PaperViewSet, basename='papers')
router.register(r'api/subjects', SubjectViewSet, basename='subjects')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Elibrary Admin Pannel"

