#!/usr/local/bin/python3

import requests
import sys
import os

if len(sys.argv) < 2:
    print("\n* Movie Title Is Required \n")
    print("Usage: python3 moviesinfo.py [ Movie Title ]\n")
else:
    api_token = os.environ['api_token']
    title = sys.argv[1]
    api_url = 'http://www.omdbapi.com/?t={}&apikey={}'.format(title, api_token)
    data = requests.get(api_url).json()
    title = data['Title']
    year = data['Year']
    rtomatoes_rating = data['Ratings'][1]['Value']
    imdb_rating = data['imdbRating']
    actors = data['Actors']
    production = data['Production']
    awards = data['Awards']
    website = data['Website']

    print('\nTitle : {} \nYear : {} \nRotten Tomatoes : {} \nIMDb : {} \nActors : {} \nProduction : {} \nAwards : {} \nWebsite : {}\n'.format(
        title, year, rtomatoes_rating, imdb_rating, actors, production, awards, website))
