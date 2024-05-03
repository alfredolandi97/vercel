from django.shortcuts import render
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    #id = int(request.GET["id"])
    id=1
    """
    Recommender calcola le raccomandazioni sulla base delle preferenze dell'id x
    Filla la lista da passare in JSON
    """
    rec_list = []
    
    for i in range(10):
        rec_list.append(random.randint(1, 1001))
    
    return JsonResponse({id:rec_list})