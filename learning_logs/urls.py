"""Defines URL patterns for learning_logs App"""
from django.urls import path
from . import views

app_name='learning_logs'
urlpatterns=[
    #Home Page
    path('', views.index, name='index'),
    # Topic page that displays all the topics
    path('topics/', views.topics, name='topics'),
    #DEtail page for each topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #New topic page
    path('new_topic/', views.new_topic, name='new_topic')
    


]