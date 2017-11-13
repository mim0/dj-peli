from django.http import JsonResponse

from .models import Pelicula, Actor

def pelis(request):
    peliculas = Pelicula.objects.prefetch_related('actores')

    pelis = list(map(lambda x : x.to_api_obj(), peliculas))

    return JsonResponse(pelis, safe=False)
