from django.shortcuts import render
from django.http import JsonResponse
import random
import requests
import pandas as pd

# Create your views here.
def home(request):
    id = int(request.GET["id"])

    data_path = "cals/resources/"
    data_file_name = data_path + "output.csv"

    
    recommendations = pd.read_csv(
        filepath_or_buffer=data_file_name,
        sep=","
    )

    rec_list = []

    recommendationsList = []
    isUserKnown = False
    if(id in recommendations["user_id"]):
        isUserKnown = True
        userRecommendations = recommendations[recommendations["user_id"]==id]
        recommendationsList = list(userRecommendations["item_list"])
        recommendationsList = recommendationsList[0].split()
    
    for i in range(10):
        if(isUserKnown):
            series_id = int(recommendationsList[i])
        else:
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