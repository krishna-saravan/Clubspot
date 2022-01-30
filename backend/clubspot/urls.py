"""clubspot URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from students.views import profile_view, register_view
from events.views import CreateEvent,UpdateEvent,register_event,event_detail,event_list
from clubs.views import  ClubCreation,club_list,clubdetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/register', register_view.as_view()),
    path('accounts/profile', profile_view),
    path('events', event_list),
    path('events/add', CreateEvent.as_view()),
    path('events/update/<id>',UpdateEvent.as_view()),
    path('events/register', register_event),
    path('events/<pk>',event_detail),
    path('clubs/add', ClubCreation.as_view()),
    path('clubs', club_list),
    path('clubs/detail/<pk>', clubdetail),
]