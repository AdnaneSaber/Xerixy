from django.urls import path
from . import views


urlpatterns = [
    path('phone/', views.phoneClick_view.as_view(), name='phoneApi'),
    path('db3/', views.db_view.as_view()),
]
