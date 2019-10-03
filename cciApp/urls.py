from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('course', views.course, name="course"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('category/<str:name>', views.category, name="category"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
]