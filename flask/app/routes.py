
import requests
import json
import nltk
import spotipy
import random
import spotipy
import pandas as pd
import numpy as np
from numpy import pi
import sentiments
import bokeh.plotting as bk
from bokeh.embed import autoload_server
from bokeh.document import Document
from bokeh.resources import CDN
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.io import output_file, show
from collections import OrderedDict
from bokeh.charts import Bar, output_file, show
import numpy as np
from alchemyapi import AlchemyAPI
from flask import Flask, render_template, request, jsonify
from forms import LoginForm
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = Flask(__name__)
app.config.from_object('config')



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/commits', methods=['POST'])
def hello():

    sad_uri = 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V'
    happy_uri = 'spotify:artist:7MhMgCo0Bl0Kukl93PZbYS'

    spotify = spotipy.Spotify()
    sad_results = spotify.artist_top_tracks(sad_uri)
    happy_results = spotify.artist_top_tracks(happy_uri)

    sad = []
    happy = []

    for track in sad_results['tracks'][:10]:
        sad.append(str(track['preview_url']))

    for track in happy_results['tracks'][:10]:
        happy.append(str(track['preview_url']))

    name=request.form['name']
    url2="https://api.github.com/users/"+name+"/repos"
    ram='zachbpd'
    auth = "d7852482e5450c9a52e48a108bf95e24de838c58"
    repos = requests.get(url2, auth=(ram,auth)).json()
    words=""
    tokens=[]
    for repo in repos:
        x=repo['name']
    for repo in repos:
        repo_name=repo['name']
        commit_url="https://api.github.com/repos/"+name+"/"+repo_name+"/commits"
        all=requests.get(commit_url, auth=(ram,auth)).json()
        for a in all:
            if(type(a) is dict):
                last=a['sha']
                x=str(a['commit']['message'])
                y=nltk.tokenize.regexp_tokenize(x, r'\w+')
                y=[q.lower() for q in y if len(q)>3 and q!="__init__"]
                tokens+=y
                words=words+" ".join(y)
    res=""
    score="0"
    freq= nltk.FreqDist(tokens).most_common(7)
    xs=[]
    ys=[]
    for (a,b) in freq:
        xs.append(a)
        ys.append(b)
    di = {'values':ys, 'names': xs}
    df = pd.DataFrame(di)
    song = ""
    qq={'a':2}
    output_file("tutorial_sharing.html")
    plot = Bar(df,'names', values='values', title="test chart",xlabel="Words", ylabel="Frequency")
    alchemyapi = AlchemyAPI()
    response = alchemyapi.sentiment('text', words)
    if response['status'] == 'OK':
        res=response['docSentiment']['type']
        if(res =="positive"):
            song = random.choice(happy)
        else:
            song = random.choice(sad)
    if 'score' in response['docSentiment']:
        score=response['docSentiment']['score']
    script, div = components(plot)
    return render_template('commits.html', script=script, div=div,score=score,res=res,name=name, song = song)


if __name__ == '__main__':
    app.run(debug=True)
