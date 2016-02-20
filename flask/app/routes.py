import requests
import requests_cache
import json

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
    auth='00abf00f9ba10bd2f2187aa273b8b8cfa940fcb3'
    repos = requests.get(url2,auth=(ram,auth)).json()
    commits=[]
    for repo in repos:
        x=repo['name']
        commits+=x
        f.write(x)
    for repo in repos:
        repo_name=repo['name']
        commits+=repo_name
        f.write("NAME: "+repo_name+"\n\n\n")
        commit_url="https://api.github.com/repos/"+name+"/"+repo_name+"/commits"
        all=requests.get(commit_url,auth=(ram,auth)).json()
        for a in all:
            if(type(a) is dict):
                x=unicode(a['commit']['message'])
                commits+=x
                f.write(x)
    f.close()
    return render_template('commits.html', name=name,commits=commits)

if __name__ == '__main__':
    app.run(debug=True)
