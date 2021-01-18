"""PyCrashCourseChap18Django URL Configuration

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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from learning_logs import views

app_name = "learning_logs"
app_name_2 = "users"

urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'', include(('learning_logs.urls', app_name), namespace="learning_logs")),
	url(r'^users/', include(('users.urls', app_name_2), namespace="users")),
	# 注意，在'^users/'后面不加dollar符号
]
