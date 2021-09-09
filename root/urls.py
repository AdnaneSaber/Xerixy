from django.urls import path
from . import views


urlpatterns = [
    path('phone/', views.phoneClick_view.as_view(), name='phoneApi'),
    path('page/', views.Page_view.as_view()),
    path('content/<int:id>/', views.Content_view.as_view()),
    path('service/', views.Service_view.as_view()),
    path('theme/', views.Theme_view.as_view()),
    path('db3/<str:name>', views.db_view.as_view()),
    path('external/', views.ExternalTools_view.as_view()),
]
