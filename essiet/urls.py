from django.urls import path

from . import views
from .views import HomeView, JobDetailView, AddJobView, JobUpdateView, JobDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('jobs/<int:pk>', JobDetailView.as_view(), name='job-detail'),
    path('post_job', AddJobView.as_view(), name='post_job'),
    path('jobs/edit/<int:pk>', JobUpdateView.as_view(), name='job-edit'),
    path('jobs/<int:pk>/delete', JobDeleteView.as_view(), name='job-delete'),
    path('contacts', views.contacts, name='contacts'),
    path('aboutus', views.aboutus, name='aboutus'),
]