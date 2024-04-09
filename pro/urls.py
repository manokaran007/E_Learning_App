"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.home,name='home'),
    path('feedback',views.feedback,name='feedback'),
    path('course',views.course,name='course'),
    path('computer',views.computer,name='computer'),
    path('com1',views.com1,name='com1'),
    path('com2',views.com2,name='com2'),
    path('com3',views.com3,name='com3'),
    path('com4',views.com4,name='com4'),
    path('com5',views.com5,name='com5'),
    path('com6',views.com6,name='com6'),
    path('com7',views.com7,name='com7'),
    path('com8',views.com8,name='com8'),
    path('computer_quiz',views.comtest,name='comtest'),
    path('maths',views.maths,name='maths'),
    path('mat1',views.mat1,name='mat1'),
    path('mat2',views.mat2,name='mat2'),
    path('mat3',views.mat3,name='mat3'),
    path('mat4',views.mat4,name='mat4'),
    path('mat5',views.mat5,name='mat5'),
    path('mat6',views.mat6,name='mat6'),
    path('mat7',views.mat7,name='mat7'),
    path('mat8',views.mat8,name='mat8'),
    path('maths_quiz',views.mattest,name='mattest'),
    path('english',views.english,name='english'),
    path('eng1',views.eng1,name='eng1'),
    path('eng2',views.eng2,name='eng2'),
    path('eng3',views.eng3,name='eng3'),
    path('eng4',views.eng4,name='eng4'),
    path('eng5',views.eng5,name='eng5'),
    path('eng6',views.eng6,name='eng6'),
    path('eng7',views.eng7,name='eng7'),
    path('eng8',views.eng8,name='eng8'),
    path('english_quiz',views.engtest,name='engtest'),
    path('tamil',views.tamil,name='tamil'),
    path('tam1',views.tam1,name='tam1'),
    path('tam2',views.tam2,name='tam2'),
    path('tam3',views.tam3,name='tam3'),
    path('tam4',views.tam4,name='tam4'),
    path('tam5',views.tam5,name='tam5'),
    path('tam6',views.tam6,name='tam6'),
    path('tam7',views.tam7,name='tam7'),
    path('tam8',views.tam8,name='tam8'),
    path('tamil_quiz',views.tamtest,name='tamtest'),
    path('Tamilleaderboard/', views.leaderboard, name='leaderboard'),
    path('Englishleaderboard/', views.eleaderboard, name='eleaderboard'),
    path('Mathsleaderboard/', views.mleaderboard, name='mleaderboard'),
    path('Computerleaderboard/', views.cleaderboard, name='cleaderboard'),
    path('game',views.game,name='game'),
    path('lb',views.lb,name='lb'),
    path('abc/',views.abc,name='abc'),
    
    path('click/',views.click,name='click'),
    path('cube/',views.cube,name='cube'),
    path('hangman/',views.hangman,name='hangman'),
    
    path('tower/',views.tower,name='tower'),
    path('chess/',views.chess,name='chess'),
    path('blind1/',views.blind1,name='blind1'),
    path('blind2/',views.blind2,name='blind2'),
    path('blind3/',views.blind3,name='blind3'),
    path('blind4/',views.blind4,name='blind4'),
]
