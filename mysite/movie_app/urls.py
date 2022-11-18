from django.urls import path


from .views import MovieView

app_name="movie_app"
urlpatterns = [
    path("",MovieView.as_view(),name='index'),
]
