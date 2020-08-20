from django.shortcuts import render
import requests
import json
from newsapi import NewsApiClient

# Create your views here.
def home(request):
	news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=066f8e804c0246ce8638e8aac0369395')
	api = json.loads(news_api_request.content)

	context ={
	   'api':api,
	}
	return render(request, 'home.html',context)
