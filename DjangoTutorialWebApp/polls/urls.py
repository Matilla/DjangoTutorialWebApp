'''
Created on Jun 18, 2018

@author: Administrator
'''
from django.urls import path

from . import views

''' Se define un namespace para las URLs de la aplicacon polls, esto sirve para diferenciar las URLs de otras apps dentro de un projecto de Django '''
app_name = 'polls'
""" Se definen las URLs y las vistas que se corresponden a esas URLS """
'''  Se cambian las URLs para usar visas genericas, definidas abajo
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
''' 

''' Se pasa a usar vistas genericas de Django en vez de las vistas normales donde aplica, por ejemplo para las vistas index, detail y results''' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]