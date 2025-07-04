"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from base import views
from pages.views import PageListView

from .views import (
    PageListView, PageDetailView, PageCreateView,
    PageUpdateView, PageDeleteView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', PageListView.as_view(), name='page-list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('pages/crear/', PageCreateView.as_view(), name='page-create'),
    path('pages/<int:pk>/editar/', PageUpdateView.as_view(), name='page-edit'),
    path('pages/<int:pk>/borrar/', PageDeleteView.as_view(), name='page-delete'),
    path('', include('pages.urls')),
]
