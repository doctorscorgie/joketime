from django.urls import path
from . import views

app_name='jokes'
urlpatterns=[
    #Home page
    path('',views.index,name='index'),
    path('joketypes',views.joketypes,name='joketypes'),
    path('joketypes/<int:topic_id>',views.joketype,name='joketype'),
]