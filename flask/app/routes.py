import requests
import requests_cache
import json
import nltk
import random
import unirest
import sentiments
from alchemyapi import AlchemyAPI
from flask import Flask, render_template, request, jsonify
from forms import LoginForm

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
    auth= '5dc6fe61936907c04d3e424ef42f688c26ef770f'
    repos = requests.get(url2,auth=(ram,auth)).json()
    words=""
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
                words=words+" ".join(y)
                f.write(x)
    f.close()
    alchemyapi = AlchemyAPI()
    response = alchemyapi.sentiment('text', words)
    res=""
    score="0"
    if response['status'] == 'OK':
        res=response['docSentiment']['type']

    if 'score' in response['docSentiment']:
        score=response['docSentiment']['score']

    return render_template('commits.html', name=name,res=res,score=score)

if __name__ == '__main__':
    app.run(debug=True)
