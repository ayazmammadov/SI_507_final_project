import requests
import json
import sys
import csv
from bs4 import BeautifulSoup


baseurl = 'https://www.imdb.com/'
catalog_url = baseurl + '/chart/top/?ref_=nv_mv_250'
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
list_of_movies = []
json_file = []


CACHE_FNAME = 'cache.json'

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTIONARY = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTIONARY = {}

def get_key(url):
  return url

def make_request_cache(url, header):
    unique_ident = get_key(url)
    if unique_ident in CACHE_DICTIONARY:
        print("Getting cached data...")
        return CACHE_DICTIONARY[unique_ident]

    ## fetch the data, add it to the cache,
    ## write the cache to file
    else:
        print("Making a request for new data...")
        resp = requests.get(url, headers=header)
        CACHE_DICTIONARY[unique_ident] = resp.text
        json_cache = json.dumps(CACHE_DICTIONARY)
        fw = open(CACHE_FNAME,"w")
        fw.write(json_cache)
        fw.close()
        return CACHE_DICTIONARY[unique_ident]



class MovieList():
    def __init__(self, movieHref ,director, actor, movieName ,releaseDate, poster_href):
        self.href = movieHref
        self.dir = director
        self.actor = actor
        self.movieName = movieName
        self.releaseDate = releaseDate
        self.poster = poster_href
        self.genre = " "

    def __str__(self):
        movie_string= 'the movie name is '+ self.movieName + ', directed by'+ self.dir +'. The release date is'+ self.releaseDate + '. The main actor is' + self.actor + '. Genre is' + self.genre
        return movie_string

    def detailed_info(self,details_url):
        request2 = make_request_cache(details_url, header)
        beat_soup = BeautifulSoup(request2, 'html.parser')
        new_one = beat_soup.find_all(class_='canwrap')
        self.genre = new_one[2].find('a').text
        return self.genre



def scrapeIMDB ():
    text_cache = make_request_cache(catalog_url, header)
    text_soup = BeautifulSoup(text_cache, 'html.parser')
    content_list = text_soup.find(class_= 'lister')
    html_body = content_list.find('tbody')
    tb_rows = html_body.find_all('tr')

    for child in tb_rows[0:10]:
        item = {}
        titleColumn = child.find(class_ = 'titleColumn')
        movieHref =  titleColumn.find('a')['href']
        director = titleColumn.find('a')['title'].split(',')[0]
        actor = titleColumn.find('a')['title'].split(',')[1]
        movieName = titleColumn.find('a').text
        releaseDate = child.find(class_ = 'secondaryInfo').text

        poster_col = child.find(class_ = 'posterColumn')
        poster_href = poster_col.find('img')['src']

        details_url = baseurl + movieHref

        movie_item = MovieList(movieHref, director, actor , movieName , releaseDate, poster_href)
        genre = movie_item.detailed_info(details_url)
        list_of_movies.append(movie_item)

        item['movieHref'] = movieHref
        item['director'] = director
        item['actor'] = actor
        item['movieName'] = movieName
        item['releaseDate'] = releaseDate
        item['poster_href'] = poster_href
        item['genre'] = genre

        json_file.append(item)

    with open('movie_data.csv', 'w', newline='') as cfile:
        s_writer = csv.writer(cfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        s_writer.writerow(["movieName","director","actor","genre","movieHref","poster_href","releaseDate"])
        for item in json_file:
            s_writer.writerow([item['movieName'],item['director'],item['actor'],item['genre'],item['movieHref'],item['poster_href'],item['releaseDate']])
    cfile.close()
    

    return list_of_movies

