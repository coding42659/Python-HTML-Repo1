from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from testing import views
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home),
  #  path('', TemplateView.as_view(template_name="main.html")),
    path('admin/', admin.site.urls),
    re_path(r'^main/$', views.main, name='main'),
    
]