
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet
from applications.views import ApplicationViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include (router.urls)),
    path('api-token-auth/', obtain_auth_token),


]
