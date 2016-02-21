import requests
import requests_cache
import json
import nltk
import random
import unirest
import sentiments
from bokeh.plotting import figure, output_file, show,line
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
requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


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
    f = open('results', 'w')
    name=request.form['name']
    url2="https://api.github.com/users/"+name+"/repos"
    ram='comRamona'
    #auth= '95c8773ff13b235694ee47b9700790adf1e3cf78'
    auth=""
    repos = requests.get(url2,auth=(ram,auth)).json()
    words=""
    tokens=[]
    for repo in repos:
        x=repo['name']
        f.write(x)
    for repo in repos:
        repo_name=repo['name']
        f.write("NAME: "+repo_name+"\n\n\n")
        commit_url="https://api.github.com/repos/"+name+"/"+repo_name+"/commits"
        all=requests.get(commit_url,auth=(ram,auth)).json()
        for a in all:
            if(type(a) is dict):
                x=str(a['commit']['message'])
                y=nltk.tokenize.regexp_tokenize(x, r'\w+')
                if(len(y)>2):
                    tokens+=y
                words=words+" ".join(y)
                f.write(x)
    f.close()
    res=""
    score="0"
    freq= nltk.FreqDist(tokens).most_common(50)
    x_1=[]
    y_1=[]
    for a,b in freq:
        x_1.append(a)
        y_1.append(b)
    snippet=build_plot(x_1,y_1)
    """alchemyapi = AlchemyAPI()
    response = alchemyapi.sentiment('text', words)
    if response['status'] == 'OK':
        res=response['docSentiment']['type']

    if 'score' in response['docSentiment']:
        score=response['docSentiment']['score']
     """
    return render_template('commits.html', name=name,res=res,score=score,snippet=snippet)

""def build_plot(x,y):

    # Set the output for our plot.

    #output_file('plot.html', title='Plot')

    # Create some data for our plot.

    # Create a line plot from our data.

     snippet=""

    # Create an HTML snippet of our plot.

    #snippet = curplot().create_html_snippet(embed_base_url='../static/js/', embed_save_loc='./static/js')

    # Return the snippet we want to place in our page.

    return snippet
if __name__ == '__main__':
    app.run(debug=True)
