from django.urls import path
from . import views


urlpatterns = [
    path('phone/', views.phoneClick_view.as_view(), name='phoneApi'),
    path('db3/<str:name>', views.db_view.as_view()),
    path('external/', views.ExternalTools_view.as_view()),
]
