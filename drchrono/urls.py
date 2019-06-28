from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()
from drchrono.views import *


urlpatterns = [
    url(r'^setup/$', SetupView.as_view(), name='setup'),
    url(r'^welcome/$', DoctorWelcome.as_view(), name='welcome'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('social_auth_drchrono.urls', namespace='social_auth')),
    url(r'^complete/drchrono/$', DoctorWelcome.as_view(), name='complete_dr'),
]