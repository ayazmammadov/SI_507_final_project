from flask import Flask, render_template, session, redirect, url_for, request
from crawlimdb import scrapeIMDB
from youtubeAPI import searchYoutube

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    movie_data = scrapeIMDB()
    return render_template('index.html', movie_data = movie_data)

@app.route('/movie/<movie_name>')
def Youtube(movie_name):
    youtube_url = searchYoutube(movie_name)
    return render_template('detail.html', url = youtube_url)


app.run( host = 'localhost',port= 8090, debug=True)
