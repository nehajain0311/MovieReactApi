from django.urls import path



from .views import MovieViewApi,MovieDetailApi

urlpatterns = [
    path("",MovieViewApi.as_view()),
    path("<int:pk>/",MovieDetailApi.as_view()),

] 
