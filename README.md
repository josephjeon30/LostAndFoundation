# MyMovieList by LostAndFoundation
## Roster
--- 
* Joseph: PM, Frontend Manager
* Nakib: Lead database manager 
* Yat Long: Middleware (Flask)
* Sasha: Database


## Description
---
* We will have a homepage that includes rows of different movies by genre
* Each movie will have a card which includes the movie poster and info about the movie
* Once you click on each movie card, you will get taken to a webpage with information about the movie (which includes director, cast, IMDB rating, places to stream the movie and a movie trailer embedded).

## APIs
---
- [OMDB API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_OMDbAPI.md)
- [Watchmode API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_WatchmodeAPI.md)
- [TheCatAPI](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_CatAPI.md)

## Launch codes
---
### Cloning:
	git clone git@github.com:josephjeon30/LostAndFoundation.git
### Virtual Environment:
#### Change into the LostAndFoundation directory:
	cd LostAndFoundation
#### Create the virtual environment:
	python3 -m venv venv
#### Activate the virtual environment:
	. venv/bin/activate
#### Install requirements:
	pip install -r requirements.txt
#### Run Flask app:
	python3 app/__init__.py
