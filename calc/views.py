from django.shortcuts import render
from django.http import JsonResponse
import random
import requests

# Create your views here.
def home(request):
    id = int(request.GET["id"])
    #id=1
    """
    Recommender calcola le raccomandazioni sulla base delle preferenze dell'id x
    Filla la lista da passare in JSON
    """
    rec_list = []
    
    for i in range(10):
        series_id = random.randint(1, 48964)
        response = requests.get('https://www.episodate.com/api/show-details?q=' + str(series_id)).json()
        series = {
            "id": response["tvShow"]["id"],
            "name": response["tvShow"]["name"],
            "description": response["tvShow"]["description"],
            "startDate": response["tvShow"]["start_date"],
            "status": response["tvShow"]["status"],
            "network": response["tvShow"]["network"],
            "thumbnail": response["tvShow"]["image_thumbnail_path"],
            "rating": response["tvShow"]["rating"],
            "genres": response["tvShow"]["genres"],
            "countdown": response["tvShow"]["countdown"],
            "episodes": response["tvShow"]["episodes"]
            }
        rec_list.append(series)
    
    return JsonResponse(rec_list, safe=False)