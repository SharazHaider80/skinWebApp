"""muscle_movement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import re_path, include, path
from muscle_movement import views, settings, muscle_views
from muscle_movement.decorators import login_required

urlpatterns = [
    re_path(r'^$', muscle_views.MainMuscle.as_view()),
    re_path(r'^login/$', views.Login.as_view()),
    re_path(r'^forgot_password/$', views.ForgotPassword.as_view()),
    re_path(r'^logout/$', views.Logout.as_view()),
    re_path(r'^check_muscle/$', muscle_views.MainMuscle.as_view()),

    # for heroku deployment!
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('admin/', admin.site.urls),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
