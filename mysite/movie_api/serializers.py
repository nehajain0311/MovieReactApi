from rest_framework import serializers


from movie_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    #image cant be used in fields before serilaizing to special imagefield type as its not text format
    image=serializers.ImageField(max_length=None, use_url=True) #use_url means we are going to use a specific url for image locations
    class Meta():
        model=Movie
        fields=['id','name','description','ratings','image']