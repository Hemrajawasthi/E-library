from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

from library import views
from library.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')
# router.register(r'semester', SemesterViewSet, basename='semester')
# router.register(r'note', NoteViewSet, basename='note')
# router.register('program', ProgramViewSet, basename='program')
# router.register('notes', api_notess, basename='notess')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/user_api/', views.api_notes ),
    path('api/notes', api_notes, name='notes'),
    path('api/programs', api_program, name='programs'),
    path('api/semesters', api_semester, name='semesters'),
    path('api/users', api_users, name='users'),
    path('api/papers', api_oldquestionpaper, name='papers'),
    path('api/syllabus', api_syllabus, name='papers'),

    # path('api/users/{id}', api_users, name='users'),





    # path('auth/', include('library.urls'))


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', views.home, name='home'),
#     path('api/', include('api.urls')),
#
# ]

admin.site.site_header = "Elibrary Admin Pannel"

