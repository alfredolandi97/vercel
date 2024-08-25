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
            "permalink": response["tvShow"]["permalink"],
            "url": response["tvShow"]["url"],
            "description": response["tvShow"]["description"],
            "descriptionSource": response["tvShow"]["description_source"],
            "start_date": response["tvShow"]["start_date"],
            "end_date": response["tvShow"]["end_date"],
            "country": response["tvShow"]["country"],
            "status": response["tvShow"]["status"],
            "runtime": response["tvShow"]["runtime"],
            "network": response["tvShow"]["network"],
            "youtube_link": response["tvShow"]["youtube_link"],
            "image_path": response["tvShow"]["image_path"],
            "image_thumbnail_path": response["tvShow"]["image_thumbnail_path"],
            "rating": response["tvShow"]["rating"],
            "rating_count": response["tvShow"]["rating_count"],
            "countdown": response["tvShow"]["countdown"],
            "genres": response["tvShow"]["genres"],
            "pictures": response["tvShow"]["pictures"],
            "episodes": response["tvShow"]["episodes"]
            }
        rec_list.append(series)
    
    return JsonResponse(rec_list, safe=False)