# Movies Info

### Overview

Movies Info is a python program that uses OMDb API to get the movie information. It is deployed and run inside a docker container.

### API Token

- You have to register your email on http://www.omdbapi.com/apikey.aspx to get your token in order to retrieved information from OMDb.

### Things You Need To Know

- Basic Knowledge of - Python - Working of API - Docker

### Instructions To Run The Program

```
   1) Clone the repository

	     git clone https://github.com/mohsinzaheer25/moviesinfo.git

   2) Update the token obtain from OMDb in your email inside env_file.

   3) Build the docker images

          docker build -t moviesinfo .

      **Note:** Make sure you are inside the folder where Dockerfile is.

   4) Run the docker container

          docker run -itd --env-file=./env_file --name moviesinfo moviesinfo:latest

   5) Search the movie title to get the information of it

          docker exec -it ca505539875 /app/moviesinfo.py transformer

     ** Note:** Replace container id (e.g. ca505539875) with your container id from step 4
```

### Expect Output

```
Title : Fast & Furious 6
Year : 2013
Rotten Tomatoes : 70%
IMDb : 7.1
Actors : Vin Diesel, Paul Walker, Dwayne Johnson, Jordana Brewster
Production : Universal Pictures
Awards : 9 wins & 21 nominations.
Website : http://www.thefastandthefurious.com/
```
