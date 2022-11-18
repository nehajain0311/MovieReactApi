from django.shortcuts import render
from rest_framework import generics
from movie_app.models import Movie
from .serializers import MovieSerializer

# Create your views here.

#this will just display data with get method
# class MovieViewApi(generics.ListAPIView):

#this will now display and create new objects via get and post methods
class MovieViewApi(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
    
#this will just retrieve the specific data object detail with get method    
#class MovieDetailApi(generics.RetrieveAPIView):

#this will just retrieve the specific data object detail and also update it with get and put method    
# class MovieDetailApi(generics.RetrieveUpdateAPIView):

#this will retrieve the specific data object detail, update and delete it with get, put and delete method  
class MovieDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer