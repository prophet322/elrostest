from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('jedi', views.get_jedi, name='jedi'),
    path('candidate-list/<int:candidat_id>/', views.candidate_list, name='candidate_list'),
    path('candidate', views.get_candidate, name='candidate'),
    path('test', views.test_candidate, name='test'),

]