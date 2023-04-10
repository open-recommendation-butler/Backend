"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework.authtoken import views
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path("", index, name='index'),
    path("api/admin/", admin.site.urls),
    path("api/article/", include('article.urls')),
    path("api/category/", include('category.urls')),
    path("api/portal/", include('portal.urls')),
    path("api/topic/", include('topic.urls')),
    path("api/suggestion/", include('suggestion.urls')),
    path("api/logger/", include('logger.urls')),
    path('api/search/', include('search.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/api-token-auth/', views.obtain_auth_token)
    ]