from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie
    
# Create your views here.
class MovieView(ListView):
    model=Movie
    template_name='movie_app/Movies.html'
    context_object_name='movies'
    
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)

    #     context['movies'] = Movie.objects.all()
    #     # for img in context['movies']:
    #     #     print (img.image.url)
    #     return context
    